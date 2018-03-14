import random

class Product:
    def __init__(self, id, name, price, inventory, description=''):
        self.id = id
        self.name = name
        self.price = price
        self.inventory = inventory
        self.description = description

class Reservation:
    def __init__(self, product, redeem):
        self.product = product
        self.redeem_code = redeem

inventory = {
    '0': Product('0', 'Powerthirst Shocklate', 1.00, 10),
    '1': Product('1', 'Brawndo', 1.50, 10, 'The thirst mutilator'),
    '2': Product('1', 'Soylent Green', 0.50, 100, 'Totally not people')
}

def create_redeem_code():
    return ''.join(random.choice('0123456789ABCDEF') for i in range(16))

def get_products():
    return inventory.values()

def get_product(id):
    return inventory.get(id)

def reserve_product(id):
    product = inventory.get(id)

    if(product is None or product.inventory <= 0):
        return None
    product.inventory -= 1

    return Reservation(product, create_redeem_code())

def release_product_reservation(id):
    product = inventory.get(id)

    if(product is None):
        return False

    product.inventory += 1
    return True
