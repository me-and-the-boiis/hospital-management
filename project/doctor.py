from flask import *
from . import db

doctor = Blueprint('doctor', __name__)
conn = db.connect()
cursor = conn.cursor()

@doctor.route('/doctor', methods=['GET', 'POST'])
def doctorWorkspace():
    cursor.execute("SELECT * FROM patient")
    data = cursor.fetchall()
    print("Hemlllo----------------")
    return render_template('Doctor/index.html', data = data)