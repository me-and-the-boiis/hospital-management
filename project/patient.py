from flask import *
from . import db

patient = Blueprint('patient', __name__)
conn = db.connect()
cursor = conn.cursor()

@patient.route('/patient', methods=['POST', 'GET'])
def viewPatient():
    if 'loggedin' in session:
        return render_template('patient-index.html')
    else:
        return redirect(url_for('auth.login'))
    # if request.method == 'GET':
    #     cursor.execute("SELECT * FROM patient WHERE hin = '{}'".format(hin))
    #     patient = cursor.fetchall()
    #     # print(patient)
    #     if not patient:
    #         return "NOTFOUND"
    #     return render_template('Patient/patient-info.html', patient = patient[0])


@patient.route('/patient/<hin>', methods=['POST', 'GET'])
def viewPatientProfile(hin):
    if request.method == 'GET':
        cursor.execute("SELECT * FROM patient WHERE hin = '{}'".format(hin))
        patient = cursor.fetchall()
        # print(patient)
        if not patient:
            return "NOTFOUND"
        return render_template('Patient/patient-info.html', patient = patient[0])

    elif request.method == 'POST':
        # myhin     = request.form['hin']
        # name    = request.form['name']
        phone   = request.form['phone']
        gender  = request.form['gender']
        cakeday = request.form['bday']
        addr    = request.form['addr']
        # print("CALL Update_Info_Patient('{}', '{}', '{}', '{}', '{}')".format(hin, gender=="Nam", cakeday, addr, phone))
        cursor.execute(
            'CALL Update_Info_Patient(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(hin, int(gender=="Nam"), cakeday, addr, phone)
        )
        conn.commit()
        flash('Cập nhật thông tin bệnh nhân thành công!')
        return redirect(url_for('patient.viewPatientProfile', hin = hin))

    return render_template('Patient/patient-info.html')

@patient.route('/patient/dependent/<id>', methods=['POST', 'GET'])
def viewDependentInfo(id):
    if request.method == 'GET':
        cursor.execute("SELECT * FROM dependent WHERE id = '{}'".format(id))
        dependent = cursor.fetchall()
        print(dependent)
        if not dependent:
            return "NOTFOUND"
        return render_template('Patient/dependent-info.html', dependent = dependent[0])

    elif request.method == 'POST':
        name    = request.form['name']
        email   = request.form['email']
        phone   = request.form['phone']
        rela    = request.form['relationship']
        print(name, email, phone)
        cursor.execute(
            'CALL Update_Info_Dependent(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(id, name, phone, email, rela)
        )
        conn.commit()
        flash('Cập nhật thông tin người thân thành công!')
        return redirect(url_for('patient.viewDependentInfo', id = id))

    return render_template('Patient/dependent-info.html')

@patient.route('/patient/exam-history', methods=['GET'])
def viewExaminationHistory():
    cursor.execute("SELECT * FROM dependent")
    data = cursor.fetchall()

    return render_template('Patient/examination-history.html' , dependentInfo=data)
