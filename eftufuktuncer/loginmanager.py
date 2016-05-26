__author__ = 'ufuktuncer'

from functools import wraps
from flask import session, redirect,url_for


def is_logged_in(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if session.get('logged_in') and session['logged_in']:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return decorated_function


def get_credential():
    if session.get('logged_in') and session['logged_in']:
        credential = {'login': True, 'name': session['current_user']}
    else:
        credential = {'login': False, 'name': None}

    return credential