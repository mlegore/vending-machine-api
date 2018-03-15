class CreditCard:
    def __init__(self, cc_number, expiration, security_code):
        self.cc_number = cc_number
        self.expiration = expiration
        self.security_code = security_code

class Charge:
    def __init__(self, success, error=''):
        self.success = success
        self.error = error
