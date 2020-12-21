from flask import *
from project import db

main = Blueprint('main', __name__)
conn = db.connect()
cursor = conn.cursor()

@main.route('/', methods=['GET'])
def index():
    cursor.execute("CALL Patient_InchargedOf(100002)")
    data = cursor.fetchall()

    return render_template('Doctor/index.html', data = data)
    return render_template('Patient/index.html')

@main.route('/profile')
def profile():
    return render_template('User/profile.html')
