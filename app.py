from flask import Flask, jsonify
from database.db_connection import initialize_db
from routers.userRouter import userRoutes
from flask_jwt_extended import JWTManager
import os
from flask_cors import CORS
from flask_socketio import SocketIO



app = Flask(__name__)

SECRET_KEY = os.urandom(32)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['JWT_SECRET_KEY']= "KmJdR8OS1Ahrm4UW"

CORS(app)

# Initializing soket server
soketio = SocketIO(app)

initialize_db(app)

print("CONFIG", app.config)

#BLUEPRINTS
app.register_blueprint(userRoutes, url_prefix="/user")

@app.route('/')
def server_status():
    return jsonify({"status": "Server running"})

jwt = JWTManager(app)

app.config['DEBUG'] = True

if __name__ == '__main__':
    # db.create_all()
    soketio.run(app)


