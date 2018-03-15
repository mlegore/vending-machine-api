
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
