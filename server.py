from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

server = Flask(__name__)
db = SQLAlchemy(server)

SECRET_KEY = 'key'

server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
server.config['SECRET_KEY'] = SECRET_KEY

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
