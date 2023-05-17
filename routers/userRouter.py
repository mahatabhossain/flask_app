from flask import Blueprint
from controllers.userController import userSignUp, getUser

userRoutes = Blueprint('userRouter', __name__)

@userRoutes.post('/signup')
def signUp():
    return userSignUp()

@userRoutes.get('/getuser')
def showUser():
    return getUser()