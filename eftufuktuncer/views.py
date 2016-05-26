__author__ = 'ufuktuncer'

from eftufuktuncer import app


@app.route('/')
def welcome_page():
    return 'Welcome to eftufuktuncer!'