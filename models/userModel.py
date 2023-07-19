from database.db_connection import db
from bson.timestamp import Timestamp
import datetime as dt

class Users(db.Document):
    fullName = db.StringField(required=True)
    email = db.StringField(required=True)
    password = db.StringField(required=True)
    timestamp = Timestamp(int(dt.datetime.today().timestamp()), 1)
