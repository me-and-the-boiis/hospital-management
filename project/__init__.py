from flask import Flask
from flaskext.mysql import MySQL
# from flask_mysqldb import MySQL

# init SQLAlchemy so we can use it later in our models
db = MySQL()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = '0000'
    app.config['MYSQL_DATABASE_DB'] = 'hospital_management'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'

    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # blueprint for doctor auth
    from .doctor import doctor as doctor_blueprint
    app.register_blueprint(doctor_blueprint)

    # blueprint for patient auth
    from .patient import patient as patient_blueprint
    app.register_blueprint(patient_blueprint)

    db.connect()

    return app
