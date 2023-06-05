from flask import Flask, jsonify
from database.db_connection import initialize_db
from routers.userRouter import userRoutes
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config['JWT_SECRET_KEY']= "KmJdR8OS1Ahrm4UW"

app.register_blueprint(userRoutes, url_prefix="/user")

initialize_db(app)
jwt = JWTManager(app)

# app.config['DEBUG'] = True

if __name__ == '__main__':
    app.run()


