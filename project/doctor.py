import datetime

from flask import *
from . import db

doctor = Blueprint('doctor', __name__)
conn = db.connect()
cursor = conn.cursor()

@doctor.route('/doctor', methods=['GET', 'POST', 'PUT'])
def doctorWorkspace():
    if request.method == 'GET':
        myHin = ""
        try:
            myHin = request.args['hin']
            cursor.execute('SELECT * FROM patient WHERE hin LIKE %s', myHin)
            data = cursor.fetchall()
            return render_template('Doctor/index.html', data=data[0], hin = myHin)
        except:
            return render_template('Doctor/index.html', data=None, hin = myHin)

    if request.method == 'POST':
        currentDateTime = datetime.datetime.now()
        note    = request.form['note']
        test    = request.form['test']
        xray    = request.form['xray']
        ptype   = request.form['ptype']
        diagnosis = request.form['diagnosis']
        # surgery = request.form['surgery']
        date    = request.form['date']
        doctor = 10007
        pHin = request.args['hin']
        cursor.execute(
            'CALL Insert_Prescription(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(currentDateTime, doctor, pHin, test, xray, diagnosis, ptype, date, note)
        )
        conn.commit()
        flash('Thêm đơn thuốc thành công bệnh nhân {}!'.format(pHin))
        # print(currentDateTime, doctor, pHin, test, xray, diagnosis, bool(ptype), date, note)
        return redirect(url_for("doctor.doctorWorkspace", hin=pHin))