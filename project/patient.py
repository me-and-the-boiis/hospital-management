from flask import *
from . import db

patient = Blueprint('patient', __name__)
conn = db.connect()
cursor = conn.cursor()

@patient.route('/patient/<hin>', methods=['POST', 'GET'])
def viewPatientProfile(hin):
    if request.method == 'GET':
        cursor.execute("SELECT * FROM patient WHERE hin = '{}'".format(hin))
        patient = cursor.fetchall()
        print(patient)
        if not patient: return "NOTFOUND"
        return render_template('Patient/patient-info.html',  patient = patient[0])

    elif request.method == 'POST':
        # myhin     = request.form['hin']
        # name    = request.form['name']
        phone   = request.form['phone']
        gender  = request.form['gender']
        cakeday = request.form['bday']
        addr    = request.form['addr']
        print("CALL Update_Info_Patient('{}', '{}', '{}', '{}', '{}')".format(hin, gender=="Nam", cakeday, addr, phone))
        cursor.execute(
            'CALL Update_Info_Patient(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(hin, int(gender=="Nam"), cakeday, addr, phone)
        )
        conn.commit()
        return redirect(url_for('patient.viewPatientProfile', hin=hin))

    return render_template('Patient/patient-info.html')

@patient.route('/patient/dependent', methods=['POST', 'GET'])
def viewDependentInfo():
    if request.method == 'GET':
        cursor.execute("SELECT * FROM dependent")
        data = cursor.fetchall()
        return render_template('Doctor/index.html', dependentInfo = data)

    elif request.method == 'POST':
        name    = request.form['name']
        email   = request.form['email']
        phone   = request.form['phone']
        rela    = request.form['relationship']
        cursor.execute('SELECT * FROM patient WHERE hin = ?', (hin,))

        # cursor.execute(
        #     '',
        #     (hin, name, email, phone, gender, cakeday, addr, g.user['id'])
        # )
        # db.commit()
        return redirect(url_for('patient.viewPatientProfile'))

    return render_template('Patient/dependent-info.html')

@patient.route('/patient/exam-history', methods=['GET'])
def viewExaminationHistory():
    cursor.execute("SELECT * FROM dependent")
    data = cursor.fetchall()

    return render_template('Patient/examination-history.html' , dependentInfo=data)
