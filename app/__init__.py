from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///links.db'
app.config['SECRET_KEY'] = 'super-secret'

db = SQLAlchemy(app)

from app import routes
