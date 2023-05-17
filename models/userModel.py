from database.db_connection import db

class Users(db.Document):
    fullName = db.StringField(required=True)
    email = db.StringField(required=True)
    password = db.StringField(required=True)