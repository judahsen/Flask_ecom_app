from app import db
from werkzeug.security import generate_password_hash,check_password_hash



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False, unique = True)
    email = db.Column(db.String, nullable = False, unique = True)
    password_hash = db.Column(db.String, nullable = False)
    first_name= db.Column(db.String(75))
    last_name= db.Column(db.String(75))


    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def del_user(self):
        db.session.delete(self)
        db.session.commit()

    def from_dict(self, user_dict):
        for k , v in user_dict.items():
            if k != 'password':
                setattr(self, k, v)
            else:
                setattr(self, 'password_hash', generate_password_hash(v))

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
# class Team(db.Model):
#     id= db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     pok1 = db.Column(db.Integer)
#     pok2 = db.Column(db.Integer)
#     pok3 = db.Column(db.Integer)
#     pok4 = db.Column(db.Integer)
#     pok5 = db.Column(db.Integer)

#     def __init__(self, user_id, pok1=None,pok2=None,pok3=None,pok4=None,pok5=None):
#         self.user_id = user_id
#         self.pok1 =pok1
#         self.pok2 =pok2
#         self.pok3 =pok3
#         self.pok4 =pok4
#         self.pok5 =pok5
    
#     def save_team(self):
#         db.session.add(self)
#         db.session.commit()


#Model for Product
class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    body = db.Column(db.String, nullable = False)
    price = db.Column(db.Integer, nullable = False)

    def from_dict(self, a_dict):
        self.name = a_dict['name']
        setattr(self, 'body', a_dict['body'])
        self.price = a_dict['price']

    def save_product(self):
        db.session.add(self)
        db.session.commit()

    def del_product(self):
        db.session.delete(self)
        db.session.commit()

#Model for Cart
class Cart(db.Model):
    __tablename__ = 'cart'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable= False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

        

# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(150), nullable=False)
#     price = db.Column(db.String, nullable=False)
#     description = db.Column(db.String(500), nullable=False)

#     def __init__(self, name, price , description):
#         self.name =name
#         self.price = price
#         self.description = description

#     def save_product(self):
#         db.session.add(self)
#         db.session.commit()

#     def to_dict(self):
#         return {
#             'id':self.id,
#             'name':self.name,
#             'price':self.price,
#             'description':self.description 
#         }


# class CartProduct(db.Model):
#     cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), primary_key=True)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
#     quantity = db.Column(db.Integer, default=1)
