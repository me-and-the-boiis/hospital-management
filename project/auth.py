from flask import *
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET','POST'])
def login():
    error = None
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        con = db.connect()
        cursor = con.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        match = cursor.fetchone()
        if match:
            user = match[0]
            session['loggedin'] = True
            # session['id'] = str(match['HIN'])
            session['username'] = user
            # return 'Logged in successfully!    ' + str(session['username'])
            # print(session['username'])
            # flash('You were successfully logged in' + user)
            return render_template('User/index.html')
        else:
            error = 'Invalid credentials'
    return render_template('User/login.html', error=error)

@auth.route('/signup', methods = ['GET','POST'])
def signup():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'HIN' in request.form:
        username = request.form['username']
        hin = request.form['HIN']
        password = request.form['password']
        con = db.connect()
        cursor = con.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = %s OR HIN = %s', (username, hin, ))
        match = cursor.fetchone()
        if match:
            return render_template('User/index.html')
        else:
            cursor.execute('INSERT INTO accounts VALUES (%s, %s, %s)', (hin, username, password,))
            con.commit()
    return render_template('User/signup.html')

@auth.route('/logout')
def logout():
    if 'loggedin' in session:
        session.clear()
        return render_template('User/index.html')
    return render_template('User/login.html')
