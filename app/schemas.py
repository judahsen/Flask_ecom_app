from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only = True)
    

class ProductSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str()
    price = fields.Str(required=True)
    description = fields.Int(required=True)

class CartSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str()
    body = fields.Str(required=True)
    author = fields.Int(required=True)
