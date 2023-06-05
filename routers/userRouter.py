from flask import Blueprint
from controllers.userController import registerUser, loginUser
from flask_jwt_extended import jwt_required

userRoutes = Blueprint('userRouter', __name__)

@jwt_required()
@userRoutes.post('/signup')
def signUp():
    return registerUser()

@userRoutes.post('/login')
def login():
    return loginUser()