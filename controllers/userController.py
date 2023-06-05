from flask import jsonify, request
from models.userModel import Users
import bcrypt
from flask_jwt_extended import(
    create_access_token,
    create_refresh_token
)
from database.db_connection import db


# ********************** SIGN UP USER SERVICE ******************
def registerUser():
    try:
        # Parse the incomming JSON request data and returns it.
        request_data = request.get_json()

        fullName = request_data['fullName']
        email = request_data['email']
        password = request_data['password'].encode("utf8")

        # Encrypting password
        passwordHash = bcrypt.hashpw(password, bcrypt.gensalt())
    
        # Saving data into database
        userData = Users(fullName=fullName, email=email, password=passwordHash).save()

        return jsonify({"status": "Sign up success", "data": userData})

    except Exception as e:
        print(str(e))
        return jsonify({"error": "Sign up failed"})
    

# ******************** LOGIN USER SERVICE **************************
def loginUser():
    try:
        # Get query parameters
        # userId = request.args.get('id')

        # Get data from request object
        # fullName = request.form.get('fullName')  

        # Parese the incomming JSON request data and returns it.
        bodyData = request.get_json()

        # Getting data from body
        email = bodyData['email']
        password = bodyData['password']

        if(not email and password): return jsonify({"error": "Please enter your details"})

        # Query data from database by email
        if(email):
            userDetails = Users.objects(email=email)
            print(jsonify({userDetails}))

        # Validating password
        is_valid_password = bcrypt.checkpw(str(password).encode("utf8"), str(userDetails[0].password).encode("utf8"))

        if(not is_valid_password): return jsonify({"authError": "Credentials does'nt match"})
        
        if(is_valid_password and str(userDetails[0].email) == email):
            # Generating token
            token = create_access_token(identity=str(userDetails[0].id))
            refreshToken = create_refresh_token(str(userDetails[0].id))
            print("Refresh token", refreshToken, "Token", token)

            return jsonify({"status": "Login success"}, userDetails, {"token": token})
    
    except Exception as e:
        print(str(e))
        return jsonify({"error": "Unable to login"})