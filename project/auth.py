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
        match = cursor.fetchall()
        if match:
            user = match[0]
            session['loggedin'] = True
            session['username'] = user[1]
            session['hin'] = user[0]
            flash('You were successfully logged in')
            return render_template('User/index.html')
        else:
            error = 'Invalid credentials'
    return render_template('User/login.html', error=error)

@auth.route('/signup', methods = ['GET','POST'])
def signup():
    error = None
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'HIN' in request.form:
        username = request.form['username']
        hin = request.form['HIN']
        password = request.form['password']
        con = db.connect()
        cursor = con.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = %s OR HIN = %s', (username, hin, ))
        match = cursor.fetchone()
        if not match:
            cursor.execute('INSERT INTO accounts VALUES (%s, %s, %s)', (hin, username, password,))
            con.commit()
            session['loggedin'] = True
            session['username'] = username
            session['hin'] = hin
            flash('Thành con nhà bà Công')
            return render_template('User/index.html')
        else:
            error = 'Tài khoản đã tồn tại!'
    return render_template('User/signup.html', error=error)

@auth.route('/logout')
def logout():
    if 'loggedin' in session:
        session.clear()
        return render_template('User/index.html')
    return render_template('User/login.html')
