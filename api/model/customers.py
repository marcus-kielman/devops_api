# Module: customers
# File Type: Database Table Model
# Author: Marcus X. Kielman
# Description: Database model for customers table
from marshmallow import Schema, fields, post_load


# ========================================================================
# Description: Initialize variables/entries in customers table and
#                specifies object String representation in Python
#       Input: Null
#      Output: Null
class Customers():
    def __init__(
                self, customerNumber, customerName, contactLastName,
                contactFirstName, phone, addressLine1, addressLine2,
                city, state, postalCode, country, salesRepEmployeeNumber,
                creditLimit
    ):
        self.customerNumber = customerNumber
        self.customerName = customerName
        self.contactLastName = contactLastName
        self.contactFirstName = contactFirstName
        self.phone = phone
        self.addressLine1 = addressLine1
        self.addressLine2 = addressLine2
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.country = country
        self.salesRepEmployeeNumber = salesRepEmployeeNumber
        self.creditLimit = creditLimit

    def __repr__(self):
        return '<Customers(name={self.customerNumber!r})>'.format(self=self)


# ========================================================================
# Description: Specifies variable field types for sending data to database
#       Input: Null
#      Output: Null
class CustomerSchema(Schema):
    customerNumber = fields.Int()
    customerName = fields.Str()
    contactLastName = fields.Str()
    contactFirstName = fields.Str()
    phone = fields.Str()
    addressLine1 = fields.Str()
    addressLine2 = fields.Str()
    city = fields.Str()
    state = fields.Str()
    postalCode = fields.Str()
    country = fields.Str()
    salesRepEmployeeNumber = fields.Int()
    creditLimit = fields.Number()

    # Sends POST Request Data to Database
    @post_load
    def make_customer(self, data, **kwargs):
        return Customers(**data)
