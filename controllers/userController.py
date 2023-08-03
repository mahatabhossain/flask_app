import os
from flask import jsonify, redirect, request, render_template, make_response
from models.userModel import Users
import bcrypt
from flask_jwt_extended import(
    create_access_token,
    create_refresh_token,
    set_access_cookies,
)
from database.db_connection import db
from fileinput import filename


# ********************** SIGN UP USER SERVICE ******************
def registerUser():
    try:
        # Parse the incomming JSON request data and returns it.
        request_data = request.get_json()

        fullName = request_data['fullName']
        email = request_data['email']
        password = request_data['password'].encode("utf8")

        print(fullName, email, type(password))

        # Encrypting password
        passwordHash = bcrypt.hashpw(password, bcrypt.gensalt())
    
        # Saving data into database
        print("Registration successfull")
        userData = Users(fullName=fullName, email=email, password=passwordHash).save()
        print("After Registration")

        # db.session.add(userData)
        # db.session.commit()
     
        return jsonify({"status": "Sign up success", "data": userData})

    except Exception as e:
        print(str(e))
        return jsonify({"error": "Sign up failed"})
    

# ******************** LOGIN USER SERVICE **************************
def renderLoginForm():
    return render_template('loginForm.html')

def loginUser():
    # resp = jsonify({'login': True})
    # resp = make_response()
    # resp.set_cookie('token', 'token')
    # return resp
    try:
        # Get query parameters
        # userId = request.args.get('id')

        # Get data from request object
        # fullName = request.form.get('fullName')  

        # Parese the incomming JSON request data and returns it.
        # bodyData = request.get_json()
        user_name = request.form.get('user_name')
        password = request.form.get('password')

        print(user_name, password)
        # Getting data from body
        # email = bodyData['email']
        # password = bodyData['password']

        email = user_name
        password = password

        # if(not(email and password)): return jsonify({"error": "Please enter your details"})

        # Query data from database by email
        if(email):
            userDetails = Users.objects.get_or_404(email=email)
            print("Fetched user details", userDetails.password)

        # Validating password
        is_valid_password = bcrypt.checkpw(str(password).encode("utf8"), str(userDetails.password).encode("utf8"))
        print("Password validated", is_valid_password)

        if(not is_valid_password): return jsonify({"authError": "Credentials does'nt match"})
        
        if(is_valid_password and str(userDetails.email) == email):
            # Generating token
            token = create_access_token(identity=str(userDetails.id))
            # refreshToken = create_refresh_token(identity=str(userDetails.id))
            resp = make_response(jsonify({"status": "Login success", "user": userDetails, "token": token}))
            resp.set_cookie('token', token)
            print("Cookie set successful", resp)
            print("Token", token)

            # return jsonify({"status": "Login success"}, userDetails, {"token": token})
            return resp
    
    except Exception as e:
        print(str(e))
        return jsonify({"error": "Unable to login"})
    

# ********************* UPDATE USER SERVICE *************************

def updateUser():
    try:

        body_data = request.get_json()
        id = request.args.get('id')

        print("Update service called", id)
        updateDetails = Users.objects.get_or_404(id = id)

        # fullName = body_data['fullName']
        # email = body_data['email']
        
        if(updateDetails): 
            if body_data['fullName']: updateDetails.fullName = body_data['fullName']
            if body_data['email']: updateDetails.email = body_data['email']

        # if(body_data['email']): updateDetails.email = body_data['email']

        updateDetails.save()

        return jsonify({"status": "success", "updated_details": updateDetails})
    except Exception as e:
        print(str(e))
        return {jsonify({"error": e})}

# ********************* DELETE USER SERVICE *********************************

def delete_user(id):
    try:
        # user_id = request.args.get('id')

        print("Delete user service called", id)
        user_details = Users.objects.get_or_404(id = id)
        user_details.delete()

        return(jsonify({"status": "success"}))
    
    except Exception as e:
        print(str(e))

#************************// FILE UPLOAD //*****************************

def upload_file():
    try:
        if request.method == 'POST':
            if not os.path.exists("./static/images"):
                os.makedirs("./static/images")
            file = request.files['file']
            file.save("./static/images/"+file.filename)
            return 'File upload successful'
    except Exception as e:
        return jsonify({"error": str(e)})