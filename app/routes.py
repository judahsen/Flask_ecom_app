from app import app
from flask import render_template,request
from uuid import uuid4

@app.route('/')
def land():
    return render_template('login.html')

#User Routes




#Post Routes

#  A route that shows a list of all available products
@app.get('/post')
def get_posts():
    try:
        return list(posts.values()), 200
    except:
        return {'message':"Failed to get posts"}, 400


# - A route which shows a single product (with the information of the product you just requested)
@app.get('/post/<post_id>')
def get_ind_post(post_id):
    try: 
        return posts[post_id], 200
    except KeyError:
        return {'message':"invalid post"}, 400
    
# - User should be able to add a product to their cart, but only if they are logged in
#JWT_extended
@app.post('/post')
def create_post():
    post_data = request.get_json()
    if post_data['author'] not in users:
        return {"message": "user does not exist"}, 400
    post_id = uuid4().hex
    posts[post_id] = post_data
    return {
        'message': "Post created",
        'post-id': post_id
        }, 201

# - A route (cart) that shows a list of products you’ve added into your cart as well as the total of all the items in your cart
@app.get('/post')
def get_posts():
    try:
        return list(posts.values()), 200
    except:
        return {'message':"Failed to get posts"}, 400


# - Add a route that, when called handles functionality that removes all items from your cart one time. Also a route, when hit, it removes a specific product object from the cart.
@app.delete('/post')
def delete_post():
    post_data = request.get_json()
    post_id = post_data['id']

    if post_id not in posts:
        return { 'message' : "Invalid Post"}, 400
    
    posts.pop(post_id)
    return {'message': f'Post: {post_id} deleted'}