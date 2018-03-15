import random

from models.products import Product, Reservation

class Products:
    def __init__(self):
        self.__inventory = {
            '0': Product('0', 'Powerthirst Shocklate', 1.00, 10),
            '1': Product('1', 'Brawndo', 1.50, 10, 'The thirst mutilator'),
            '2': Product('1', 'Soylent Green', 0.50, 100, 'Totally not people')
        }

    def __create_redeem_code(self):
        return ''.join(random.choice('0123456789ABCDEF') for i in range(16))

    def get_products(self):
        return self.__inventory.values()

    def get_product(self, id):
        return self.__inventory.get(id)

    def reserve_product(self, id):
        product = self.__inventory.get(id)

        if(product is None or product.inventory <= 0):
            return None
        product.inventory -= 1

        if(product.inventory < 2):
            #perhaps log that inventory is getting low
            print product.name + " inventory is low."

        return Reservation(product, self.__create_redeem_code())

    def release_product_reservation(self, id):
        product = self.__inventory.get(id)

        if(product is None):
            return False

        product.inventory += 1
        return True
