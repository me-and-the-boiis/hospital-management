from flask import *
from . import db

doctor = Blueprint('doctor', __name__)

@doctor.route('/doctor')
def doctorWorkspace():
    return render_template('Doctor/index.html')