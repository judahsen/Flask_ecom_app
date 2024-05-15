from . import ma
from .models import Product, Cart
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        include_fk = True
        load_instance = True
    
    id = ma.auto_field()
    name =ma.auto_field()

class CartSchema(ma.SQLAlchemyAutoSchema):
    items = ma.Nested(ProductSchema, many=True)
    class Meta:
        model = Cart
        include_relationships = True
        load_instance = True
