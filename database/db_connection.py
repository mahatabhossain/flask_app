from flask_mongoengine import MongoEngine
# from flask_pymongo import PyMongo
# from flask_sqlalchemy import SQLAlchemy
from dotenv import dotenv_values
import os


MONGO_URI = dotenv_values('.env')['MONGO_URI']
print(MONGO_URI)
# print(os.environ.get("MONGO_URI"))

#**************************// Connection usign MongoEngine //****************************8
db = MongoEngine()

def initialize_db(app):
    try:
        # app.config['MONGODB_SETTINGS'] = {
        # 'db': 'flask_app_db',
        # 'host': 'localhost',
        # 'port': 27017
        # }
      

        app.config['MONGODB_SETTINGS'] = {
        'host': MONGO_URI
        }
        print("DB CONNECTED")
        # db.init_app(app)
        # print('Database connected')
    except Exception as e :
        print("DB CONNECTION ERROR", str(e))

#**************************// Connection using MongoClient //****************************
# def initialize_db(app):
#     try:
#         print("initialize app called")
#         app.config["MONGO_URI"] = MONGO_URI
#         mongodb_client = PyMongo(app)
#         db = mongodb_client.db
#         print("MONGO DB", db)
#         return db
#     except Exception as e:
#         print(str(e))

#***************************// POSTGRES CONNECTION //**********************

# db = 'none'

# def initialize_db(app):
#     global db
#     try:
#         db = SQLAlchemy(app)
        
#     except Exception as e:
#         print(str(e))