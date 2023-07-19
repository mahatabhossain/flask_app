# from database.db_connection import db
from bson.timestamp import Timestamp
import datetime as dt
from database.db_connection import db

class Users(db.Document):
    fullName = db.StringField(required=True)
    email = db.StringField(required=True)
    password = db.StringField(required=True)
    # timestamp = Timestamp(int(dt.datetime.today().timestamp()), 1)


# class People(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     fullName = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), nullable=False)
#     password = db.Column(db.String(120), nullable=False)