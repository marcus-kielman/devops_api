# Module: offices
# File Type: Database Table Model
# Author: Marcus X. Kielman
# Description: Database model for offices table
from marshmallow import Schema, fields


# ========================================================================
# Description: Initialize variables/entries in customers table and
#                specifies object String representation in Python
#       Input: Null
#      Output: Null
class Offices():
    def __init__(
                self, officeCode, city, phone, addressLine1, addressLine2,
                state, country, postalCode, territory
    ):
        self.officeCode = officeCode
        self.city = city
        self.phone = phone
        self.addressLine1 = addressLine1
        self.addressLine2 = addressLine2
        self.state = state
        self.country = country
        self.postalCode = postalCode
        self.territory = territory

    def __repr__(self):
        return '<Offices(name={self.officeCode!r})>'.format(self=self)


# ========================================================================
# Description: Specifies variable field types for sending data to database
#       Input: Null
#      Output: Null
class OfficeSchema(Schema):
    officeCode = fields.Int()
    city = fields.Str()
    phone = fields.Str()
    addressLine1 = fields.Str()
    addressLine2 = fields.Str()
    state = fields.Str()
    country = fields.Str()
    postalCode = fields.Str()
    territory = fields.Str()
