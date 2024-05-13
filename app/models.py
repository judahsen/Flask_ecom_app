
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)  

    def __init__(self,username, email, password):
        self.ussername= username
        self.email =email
        self.password = generate_password_hash(password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'username':self.username
        }

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500))

    def __init__(self, name, price , description):
        self.name =name
        self.price = price
        self.description = description

    def save_product(self):
        db.session.add(self)
        db.session.commit()

# class Cart(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     user = db.relationship('User', backref='cart')
#     items = db.relationship('Product', secondary='cart_product', backref='carts')

class Team(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pok1 = db.Column(db.Integer, db.ForeignKey('pokemon.id'))
    pok2 = db.Column(db.Integer, db.ForeignKey('pokemon.id'))
    pok3 = db.Column(db.Integer, db.ForeignKey('pokemon.id'))
    pok4 = db.Column(db.Integer, db.ForeignKey('pokemon.id'))
    pok5 = db.Column(db.Integer, db.ForeignKey('pokemon.id'))

    def __init__(self, user_id, pok1=None,pok2=None,pok3=None,pok4=None,pok5=None):
        self.user_id = user_id
        self.pok1 =pok1
        self.pok2 =pok2
        self.pok3 =pok3
        self.pok4 =pok4
        self.pok5 =pok5


# class CartProduct(db.Model):
#     cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), primary_key=True)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
#     quantity = db.Column(db.Integer, default=1)
