from app import app,db
from flask.views import MethodView
from flask import render_template,request,Blueprint,jsonify
from app.models import User,Product,Cart
from app.schemas import ProductSchema,CartSchema,UserSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import cart,product
from flask_smorest import abort





#  A route that shows a list of all available products
@product.route('/products')
class Products(MethodView):

    @product.response(200, ProductSchema(many=True))
    def get(self):

        products = Product.query.all()
        return products
    
    @product.arguments(ProductSchema)
    @product.response(201, ProductSchema)
    def post(self, data):
        try:
            existing_prod = Product.query.filter_by(name=data['name']).first()
            if existing_prod:
                abort(400, message="Product already exists; try a different one.")

            product = Product()
            product.from_dict(data)
            product.save_product()
            
            return product
        
        except Exception:
            abort(500, message="Unexpected error; please try again.")



# - A route which shows a single product (with the information of the product you just requested)
@product.route('/products/<int:id>')
class SingleProduct(MethodView):

    @product.response(200, ProductSchema)
    def get(self, id):
    
        product = Product.query.get(id)

        if product:
            return product
        else:
            abort(400, error='Product not found')
        





# - A route (cart) that shows a list of products you’ve added into your cart as well as the total of all the items in your cart
@cart.route('/cart/<int:user_id>')
class CartList(MethodView):
    
    
    def get(self, user_id):
        cart_items = Cart.query.filter_by(user_id=user_id).all()

        if cart_items:
            serialized_cart = []

            for cart_item in cart_items:
                product = Product.query.get(cart_item.product_id)

                product_dict = {
                    'id': product.id,
                    'name': product.name,
                    'body': product.body,
                    'price': product.price
                }

                serialized_cart.append(product_dict)

            total_price = sum(product_dict['name'] for product_dict in serialized_cart)

            return {
                'cart': serialized_cart,
                'total_price': total_price
            }, 200
        else:
            return {'message': 'Cart is empty'}, 404

    # - Add a route that, when called handles functionality that removes all items from your cart one time.     
    def delete_all_products():
        data = request.get_json()
        user_id = data.get('user_id')
        cart_items = Cart.query.filter_by(user_id=user_id).all()
        if cart_items:
            for cart_item in cart_items:
                cart_item.delete()  
            return jsonify({'message': 'Cart cleared successfully'}), 200
        else:
            return jsonify({'message': 'Cart is already empty'}), 404
   



@cart.route('/cart/<product_id>')
class CartProducts(MethodView):

    # - User should be able to add a product to their cart, but only if they are logged in
    #JWT_extended
    @jwt_required()
    @cart.response(201, ProductSchema)
    def post(self):
        data = request.get_json()
        user_id = get_jwt_identity()
        product_id = data.get('product_id')
        product = Product.query.get(product_id)
        user = User.query.get(user_id)
        if user and product:
            added_by_user = Cart.query.filter_by(product_id = product_id).filter_by(user_id = user_id).all()
            if added_by_user:
                return product
            cartModel = Cart(user_id=user_id, product_id=product_id)
            cartModel.save()
            return product
        abort(400, message="Invalid User or Product")


#A route, when hit, it removes a specific product object from the cart.
@cart.route('/cart/<int:user_id>/<int:product_id>')
class Cart(MethodView):
  
    def delete(self, user_id, product_id):
        product = Product.query.get(product_id)
        user = User.query.get(user_id)
        if user and product:
            cart_items = Cart.query.filter_by(product_id=product_id).filter_by(user_id=user_id).all()
            if cart_items:
                for cart_item in cart_items:
                    cart_item.delete()
                db.session.commit()
                return {'message': '{product} removed from cart successfully'}, 201
            else:
                return {'message': 'Product is not in the cart'}, 404
        else:
            return {'message': 'Invalid User or Product'}, 400