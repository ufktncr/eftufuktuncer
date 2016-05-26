__author__ = 'ufuktuncer'

from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eftufuktuncer.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import eftufuktuncer.views
import eftufuktuncer.models