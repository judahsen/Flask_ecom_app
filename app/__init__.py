from flask import Flask,render_template
# from flask_smorest import Api
from config import Config
# from .api.routes import api
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
@app.route('/')
def land():
    return render_template('login.html')

app.config.from_object(Config)



# api = Api(app)
jwt = JWTManager(app)

db = SQLAlchemy()

db.init_app(app)
migrate = Migrate(app,db)
ma=Marshmallow(app)

from app.models import User,Product,Cart

from resources.post import product
app.register_blueprint(product)
from resources.post import cart
app.register_blueprint(cart)
from resources.user import bp as user_bp
app.register_blueprint(user_bp)





