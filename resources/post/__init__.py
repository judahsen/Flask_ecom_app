from flask_smorest import Blueprint

cart = Blueprint("cart", __name__, url_prefix='/cart')
product = Blueprint("products", __name__, url_prefix='/products')


from . import routes