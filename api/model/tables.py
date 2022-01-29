from marshmallow import Schema, fields


class Tables():
    def __init__(self, table_name):
        self.table_name = table_name

    def __repr__(self):
        return '<Tables(name={self.table_name!r})>'.format(self=self)


class TableSchema(Schema):
    table_name = fields.Str()
