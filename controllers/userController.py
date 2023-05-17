from flask import jsonify, request
from models.userModel import Users


################# USER SIGNUP SERVICE ###############
def userSignUp():
    try:
        #GET FORM DATA FROM REQUEST OBJECT
        # fullName = request.form.get('fullName')

        #GET JSON DATA FROM REQUEST OBJECT
        req_data = request.get_json()

        fullName = req_data['fullName']
        email = req_data['email']
        password = req_data['password']

        #GET QUERY PARAMETER 
        userId = request.args.get('id')   

        #SAVING DATA INTO DATABASE
        userData = Users(fullName = fullName, email = email, password = password ).save()

        # return jsonify({'message':'User signup successful', 'data':userData})
        # return jsonify({'status': 'User registration successfull'},userData)
        return jsonify(userData)

    except Exception as e:
        return jsonify({"status": 'User registration failed', 'error': str(e)})


################# GET USER SERVICE ###############
def getUser():
    try:
        # userDetails = Users.objects.get_or_404()
        # print(userDetails)
        for user in Users.objects:
            # print(user)
            return jsonify(user)
        # return '<h1>Hi</h1>'

    except Exception as e:
        return jsonify({"status": "Failed to retrieve user", 'error': str(e)})


    
############## UPDATE USER #####################




############## DELETE USER ######################


    