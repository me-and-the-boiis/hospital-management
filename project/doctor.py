from flask import *
from . import db

doctor = Blueprint('doctor', __name__)
conn = db.connect()
cursor = conn.cursor()

@doctor.route('/doctor', methods=['GET', 'POST', 'PUT'])
def doctorWorkspace():
    pHin = ''
    if request.method == 'POST':
        myhin   = request.form['hin']
        # cursor.execute('SELECT * FROM patient WHERE hin LIKE %s', myhin)
        # data = cursor.fetchall()
        # pHin = data[0][0]
        # return render_template('Doctor/index.html', data=data)
        return redirect(url_for("doctor.doctorWorkspace", patientHIN=myhin))

    if request.method == 'PUT':
        note    = request.form['note']
        test    = request.form['test']
        xray    = request.form['xray']
        ptype   = request.form['ptype']
        diagnosis = request.form['diagnosis']
        surgery = request.form['surgery']
        date    = request.form['date']
        doctor = 10007
        pHin = request.args['patientHIN']
        # cursor.execute(
        #     'CALL Insert_Prescription(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(date, doctor, pHin, test, xray, diagnosis, ptype, date, note)
        # )
        print(date, doctor, pHin, test, xray, diagnosis, ptype, date, note)
    try:
        myHin = request.args['patientHIN']
    except:
        return render_template('Doctor/index.html', data=(None,))
    cursor.execute('SELECT * FROM patient WHERE hin LIKE %s', myHin)
    data = cursor.fetchall()
    if not data:
        data = (None,)

    return render_template('Doctor/index.html', data = data)

