# in a real service this would go off to some payment processor as an http request, but for this we'll store in memory
# also the service probably wouldn't handle the cc number at all, but a reference to it

from models.payments import Charge

# in a real service this would go off to some payment processor as an http request, but for this we'll store in memory
# also the service probably wouldn't handle the cc number at all, but a reference to it
class Payments:
    def __init__(self):
        # initialize connection to service here
        self.__db = {
            '1234': 1.00,
            '5606': 1000.0
        }

    def charge(self, cc, amount, currency):
        limit = self.__db.get(cc.cc_number)
        if(limit == None):
            return Charge(False, 'Invalid credit card number.')
        if(limit < amount):
            return Charge(False, 'Payment declined due to credit limit.')
        return Charge(True)

    def refund(self, cc, amount):
        # refund might happen here
        pass
