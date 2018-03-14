class Product:
    def __init__(self, id, name, price, inventory, description=''):
        self.id = id
        self.name = name
        self.price = price
        self.inventory = inventory
        self.description = description

inventory = {
    '0': Product('0', 'Powerthirst Shocklate', 1.00, 10),
    '1': Product('1', 'Brawndo', 1.50, 10, 'The thirst mutilator'),
    '2': Product('1', 'Soylent Green', 0.50, 100, 'Totally not people')
}

def get_products():
    return inventory.values()

def get_product(id):
    return inventory.get(id)
