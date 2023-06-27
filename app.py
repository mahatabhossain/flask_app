from flask import Flask, jsonify
from database.db_connection import initialize_db
from routers.userRouter import userRoutes
from flask_jwt_extended import JWTManager
import os


SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.config['JWT_SECRET_KEY']= "KmJdR8OS1Ahrm4UW"

# initialize_db(app)
mongo_client_db = initialize_db(app)
app.register_blueprint(userRoutes, url_prefix="/user")

@app.route('/')
def server_status():
    return jsonify({"status": "Server running"})

jwt = JWTManager(app)
app.config['BASE_URL'] = 'http://127.0.0.1:5000'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = True
app.config['JWT_ACCESS_COOKIE_PATH'] = '/auth'
app.config['DEBUG'] = True

if __name__ == '__main__':
    app.run()


