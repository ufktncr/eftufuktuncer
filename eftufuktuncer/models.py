__author__ = 'ufuktuncer'

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from eftufuktuncer import app

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password_has = db.Column(db.String(200), unique=True)
    country = db.Column(db.String(50), unique=False)

    @property
    def password(self):
        raise AttributeError('password field is read-only')

    @password.setter
    def password(self, password):
        self.password_has = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_has, password)

    def __init__(self, username, password, country):
        self.username = username
        self.password = password
        self.country = country

    def __repr__(self):
        return self.username