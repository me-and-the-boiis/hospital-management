from flask import *
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('User/index.html')

@main.route('/profile')
def profile():
    return render_template('User/profile.html')
