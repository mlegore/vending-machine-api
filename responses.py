
def product_response(product):
    return {
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'available': product.inventory > 0
    }

def products_response(products, currency):
    return {
        'products': [product_response(product) for product in products],
        'currency': currency
    }

def product_dispense_response(reservation):
    return {
        'product': product_response(reservation.product),
        'redeem_code': reservation.redeem_code
    }
