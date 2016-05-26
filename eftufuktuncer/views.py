__author__ = 'ufuktuncer'

from eftufuktuncer import app
from flask import render_template, request, redirect, url_for, session
from eftufuktuncer.models import *


@app.route('/')
def welcome_page():
    return render_template('welcome.html'), 404


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username']:
            userlist = User.query.filter_by(username=request.form['username']).all()
            if not userlist or len(userlist) == 0 or not userlist[0].verify_password(request.form['password']):
                error = 'Username or Password is invalid. Please try again'
            else:
                session['logged_in'] = True
                session['current_user'] = userlist[0].username
                return redirect(url_for('content'))
        else:
            error = 'Username or Password is invalid. Please try again'

    return render_template('login.html', error=error), 404


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None

    if request.method == "POST":
        if not request.form['username'] or not request.form['password']:
            error='Please fill all fields'
        else:
            try:
                newuser = User(request.form['username'], request.form['password'], request.form['country'])
                db.session.add(newuser)
                db.session.commit()
                return redirect(url_for('content'))
            except:
                error = 'Oops! something went wrong. Please try again'

    return render_template('register.html', error = error), 404


@app.route('/content')
def content():
    return render_template('content.html')
