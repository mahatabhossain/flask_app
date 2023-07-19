from flask import Blueprint
from controllers.userController import registerUser, loginUser, updateUser, delete_user, renderLoginForm, upload_file
from flask_jwt_extended import jwt_required

userRoutes = Blueprint('userRouter', __name__)

@jwt_required()
@userRoutes.post('/signup')
def signUp():
    return registerUser()

@userRoutes.get('/login-page')
def loginForm():
    return renderLoginForm()

@userRoutes.post('/login')
def login():
    return loginUser()

@userRoutes.put('/update')
def update():
    return updateUser()

@userRoutes.delete('/delete/<id>')
def delete(id):
    return delete_user(id)

@userRoutes.post('/file')
def file_upload():
    return upload_file()