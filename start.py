from bottle import Bottle, route, run, install, JSONPlugin, request, HTTPError, error, response
from services import products, payments
import json
from responses import products_response, product_response, product_dispense_response

app = Bottle()

@app.get('/products')
def get_products():
    return products_response(products.get_products(), 'USD')

@app.get('/products/<id>')
def get_product(id):
    product = products.get_product(id)

    # I might have done this with a custom error class, but that seems a bit heavyweight for this simple app
    if(product is None):
        return HTTPError(status=404, body={'error': "Product not found."})
    return product_response(product)

@app.post('/purchase')
def purchase():
    # ensure we have a product, always do this before charging. chargebacks cost money
    product_reservation = products.reserve_product(request.json['product_id'])

    # Also might have used error class
    if(product_reservation == None):
        return HTTPError(status=404, body={'error': "Product not found."})

    cc = payments.CreditCard(request.json['cc_number'], request.json['expiration'], request.json['security_code'])
    charge = payments.charge(cc, product_reservation.product.price, 'USD')

    if(charge.success):
        return product_dispense_response(product_reservation)

    # if the charge didn't go through, release the inventory back into stock
    products.release_product_reservation(product_reservation.product.id)
    return HTTPError(status=401, body={'error': charge.error})

@app.error(400)
@app.error(401)
@app.error(404)
def error_handler(error):
    response.status = error.status
    return error.body

install(JSONPlugin(json_dumps=lambda body: json.dumps(body, default=json_util.default)))
run(app, host='localhost', port=8080, debug=True)
