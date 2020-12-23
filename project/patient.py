from flask import *
from . import db

patient = Blueprint('patient', __name__)
conn = db.connect()
cursor = conn.cursor()

@patient.route('/patient', methods=['POST', 'GET'])
def viewPatientProfile():
    if request.method == 'GET':
        cursor.execute("SELECT * FROM patient")
        data = cursor.fetchall()
        return render_template('Doctor/index.html', patientInfo = data)

    elif request.method == 'POST':
        name    = request.form['name']
        email   = request.form['email']
        phone   = request.form['phone']
        rela    = request.form['relationship']
        cursor.execute(
            '',
            (name, email, phone, rela, g.user['id'])
        )
        db.commit()
        return redirect(url_for('patient.viewPatientProfile'))

    return render_template('Patient/patient-info.html')

@patient.route('/patient/dependent', methods=['POST', 'GET'])
def viewDependentInfo():
    if request.method == 'GET':
        cursor.execute("SELECT * FROM dependent")
        data = cursor.fetchall()
        return render_template('Doctor/index.html', dependentInfo = data)

    elif request.method == 'POST':
        hin     = request.form['hin']
        name    = request.form['name']
        email   = request.form['email']
        phone   = request.form['phone']
        gender  = request.form['gender']
        cakeday = request.form['bday']
        addr    = request.form['addr']
        cursor.execute(
            '',
            (hin, name, email, phone, gender, cakeday, addr, g.user['id'])
        )
        db.commit()
        return redirect(url_for('patient.viewPatientProfile'))

    return render_template('Patient/dependent-info.html')

@patient.route('/patient/exam-history', methods=['GET'])
def viewExaminationHistory():
    cursor.execute("SELECT * FROM dependent")
    data = cursor.fetchall()

    return render_template('Patient/examination-history.html' , dependentInfo=data)
