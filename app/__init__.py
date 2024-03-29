from flask import Flask, Blueprint, session
import os
import sys
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from flask_bootstrap import Bootstrap

import psycopg2


app = Flask(__name__)
Bootstrap(app)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/about'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'etdvt'

from app import models
from app import about



db.create_all()
app.debug = True