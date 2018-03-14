# in a real service this would go off to some payment processor as an http request, but for this we'll store in memory
# also the service probably wouldn't handle the cc number at all, but a reference to it
db = {
    '1234': 1.00,
    '5606': 1000.0
}

class CreditCard:
    def __init__(self, cc_number, expiration, security_code):
        self.cc_number = cc_number
        self.expiration = expiration
        self.security_code = security_code

class Charge:
    def __init__(self, success, error=''):
        self.success = success
        self.error = error

def charge(cc, amount, currency):
    limit = db.get(cc.cc_number)
    if(limit == None):
        return Charge(False, 'Invalid credit card number.')
    if(limit < amount):
        return Charge(False, 'Payment declined due to credit limit.')
    return Charge(True)
