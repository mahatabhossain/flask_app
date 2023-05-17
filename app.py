from flask import Flask, jsonify
from database.db_connection import initialize_db
from controllers.userController import userSignUp
from routers.userRouter import userRoutes

app = Flask(__name__)

app.register_blueprint(userRoutes, url_prefix="/userRoutes")

initialize_db(app)

# app.config['DEBUG'] = True

if __name__ == '__main__':
    
    app.run(port=5000)


