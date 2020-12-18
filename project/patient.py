from flask import *
from . import db

patient = Blueprint('patient', __name__)

@patient.route('/patient')
def viewPatientProfile():
    return render_template('Patient/patient-info.html')

@patient.route('/patient/dependent')
def viewDependentInfo():
    return render_template('Patient/dependent-info.html')

@patient.route('/patient/exam-history')
def viewExaminationHistory():
    return render_template('Patient/examination-history.html')
