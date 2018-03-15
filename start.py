from bottle import Bottle, route, run, install, JSONPlugin, request, HTTPError, error, response
import json

from services.products import Products
from services.payments import Payments
from services.models.payments import CreditCard

from responses import products_response, product_response, product_dispense_response

app = Bottle()

# initialize services
products_db = Products()
payments_service = Payments()

@app.get('/v1/products')
def get_products():
    return products_response(products_db.get_products(), 'USD')

@app.get('/v1/products/<id>')
def get_product(id):
    product = products_db.get_product(id)

    # I might have done this with a custom error class, but that seems a bit heavyweight for this simple app
    if(product is None):
        return HTTPError(status=404, body={'error': "Product not found."})
    return product_response(product)

@app.post('/v1/purchase')
def purchase():
    # ensure we have a product, always do this before charging. chargebacks cost money
    product_reservation = products_db.reserve_product(request.json['product_id'])

    # Also might have used error class
    if(product_reservation == None):
        return HTTPError(status=404, body={'error': "Product not found."})

    cc = CreditCard(request.json['cc_number'], request.json['expiration'], request.json['security_code'])
    charge = payments_service.charge(cc, product_reservation.product.price, 'USD')

    if(charge.success):
        return product_dispense_response(product_reservation)

    # if the charge didn't go through, release the inventory back into stock
    products_db.release_product_reservation(product_reservation.product.id)
    return HTTPError(status=401, body={'error': charge.error})

@app.error(400)
@app.error(401)
@app.error(404)
def error_handler(error):
    response.status = error.status
    return error.body

install(JSONPlugin(json_dumps=lambda body: json.dumps(body, default=json_util.default)))
run(app, host='localhost', port=8080, debug=True)
