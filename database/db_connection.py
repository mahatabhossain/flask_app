from flask_mongoengine import MongoEngine
from dotenv import dotenv_values
import os

MONGO_URI = dotenv_values('.env')['MONGO_URI']
# print(MONGO_URI)

db = MongoEngine()

def initialize_db(app):
    try:
        # app.config['MONGODB_SETTINGS'] = {
        # 'db': 'flaskDB',
        # 'host': 'localhost',
        # 'port': 27017
        # }

        app.config['MONGODB_SETTINGS'] = {
        'host': MONGO_URI
        }
        
        db.init_app(app)
        print('Database connected')
    except Exception as e :
        print(str(e))
