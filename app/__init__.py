from flask import Flask

from config import Config
from .api.routes import api
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from .models import db


app = Flask(__name__)

app.config.from_object(Config)







db.init_app(app)
migrate = Migrate(app,db)
ma=Marshmallow(app)

app.register_blueprint(api)


from . import routes
from . import models



