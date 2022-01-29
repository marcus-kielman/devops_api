# Module: payments
# File Type: Database Table Model
# Author: Marcus X. Kielman
# Description: Database model for payments table
from marshmallow import Schema, fields, post_load


# ========================================================================
# Description: Initialize variables/entries in customers table and
#                specifies object String representation in Python
#       Input: Null
#      Output: Null
class Payments():
    def __init__(self, customerNumber, checkNumber, paymentDate, amount):
        self.customerNumber = customerNumber
        self.checkNumber = checkNumber
        self.paymentDate = paymentDate
        self.amount = amount

    def __repr__(self):
        return '<Payments(name={self.customerNumber!r})>'.format(self=self)


# ========================================================================
# Description: Specifies variable field types for sending data to database
#       Input: Null
#      Output: Null
class PaymentSchema(Schema):
    customerNumber = fields.Int()
    checkNumber = fields.Str()
    paymentDate = fields.Date()
    amount = fields.Number()

    # Sends POST Request Data to Database
    @post_load
    def make_payment(self, data, **kwargs):
        return Payments(**data)
