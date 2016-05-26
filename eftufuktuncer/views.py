__author__ = 'ufuktuncer'

from eftufuktuncer import app
from flask import render_template


@app.route('/')
def welcome_page():
    return render_template('welcome.html'), 404


@app.route('/login')
def login():
    error = None
    return render_template('login.html', error=error)


@app.route('/register')
def register():
    return render_template('register.html'), 404


@app.route('/content')
def content():
    return render_template('content.html')
