from app import app
from flask import render_template,request,Blueprint
from uuid import uuid4


bp = Blueprint("users", __name__, url_prefix='/users')

@app.route('/')
def land():
    return render_template('login.html')

#User Routes
