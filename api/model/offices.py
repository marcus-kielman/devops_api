from marshmallow import Schema, fields


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
