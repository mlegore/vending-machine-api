from bottle import Bottle, route, run, install, JSONPlugin
from services import products
import json
from responses import products_response, product_response

app = Bottle()

@app.get('/products')
def get_products():
    return products_response(products.get_products(), "USD")

@app.get('/products/<id>')
def get_product(id):
    return product_response(products.get_product(id))

install(JSONPlugin(json_dumps=lambda body: json.dumps(body, default=json_util.default)))
run(app, host='localhost', port=8080, debug=True)
