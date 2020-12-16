from flask import *
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('User/login.html')

@auth.route('/signup')
def signup():
    return render_template('User/signup.html')

@auth.route('/logout')
def logout():
    return 'Logout'
