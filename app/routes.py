from app import app
from flask import render_template

@app.route('/')
def land():
    return render_template('login.html')