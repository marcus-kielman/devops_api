# Module: offices
# File Type: Database Table Model
# Author: Marcus X. Kielman
# Description: Database model for database tables
from marshmallow import Schema, fields


# ========================================================================
# Description: Initialize variables/entries in customers table and
#                specifies object String representation in Python
#       Input: Null
#      Output: Null
class Tables():
    def __init__(self, table_name):
        self.table_name = table_name

    def __repr__(self):
        return '<Tables(name={self.table_name!r})>'.format(self=self)


# ========================================================================
# Description: Specifies variable field types for sending data to database
#       Input: Null
#      Output: Null
class TableSchema(Schema):
    table_name = fields.Str()
