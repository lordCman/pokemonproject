import email
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

#create our models based off our ERD\
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique = True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique = True)
    password = db.Column(db.String(300), nullable=False)

    def __init__(self, username, name, email, password):
        self.username = username
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def updateAccount(self, username, name, email, password):
        self.username = username
        self.name = name
        self.email = email
        self.password = password

    def saveUpdates(self):
        db.session.commit()
