from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config.from_object('chusentest.config')

db = SQLAlchemy(app)
from .models import guest

engine = create_engine('sqlite:///sample_flask.db')

SessionClass = sessionmaker(engine)
session = SessionClass

from chusentest import views #views.pyをimport
