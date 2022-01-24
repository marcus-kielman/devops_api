from marshmallow import Schema, fields, post_load

class Payments():
    def __init__(self, customerNumber, checkNumber, paymentDate, amount):
        self.customerNumber = customerNumber
        self.checkNumber = checkNumber
        self.paymentDate = paymentDate
        self.amount = amount
    def __repr__(self):
        return '<Payments(name={self.customerNumber!r})>'.format(self=self)

class PaymentSchema(Schema):
    customerNumber = fields.Int()
    checkNumber = fields.Str()
    paymentDate = fields.Date()
    amount = fields.Number()

    @post_load
    def make_payment(self, data, **kwargs):
        return Payments(**data)