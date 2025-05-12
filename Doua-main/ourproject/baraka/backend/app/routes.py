from flask import Blueprint, request, jsonify, current_app 
from . import db
from .models import User
from .utils import generate_confirmation_code
api_bp = Blueprint('api', __name__)

# GET /api/users - Retrieve all users
@api_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

# GET /api/users/<user_id> - Retrieve a specific user
@api_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

# POST /api/users - Create a new user
@api_bp.route('/users', methods=['POST'])
def create_user():
    userData = request.get_json()

    if User.ValidateUserData(userData):
        confirmationCode = generate_confirmation_code()
        new_user = User(userName=userData['userName'],
                        email=userData['email'],
                        password=userData['password'],
                        confirmationCode = confirmationCode)
        db.session.add(new_user)
        db.session.commit()

        #Send Confirmation code to User
        # Access the mailer from the Flask app context
        mailer = current_app.mailer
        #use it here 
        mailer.send_email(to=userData['email'], subject="Confirmation Code", body=f"Confiramtion Code is {confirmationCode}")
        
        user = User.query.filter_by(email=userData['email']).first()
        return jsonify({
            'status' : 200,
            'user': user.to_dict(),
        })
    else:
        return jsonify({
            'status' : 401,
            'error': "Invalid Informations" ,
        })
    

# POST /api/users - Create a new user
@api_bp.route('/users/confirm', methods=['POST'])
def confirm_user():
    ConfirmationData = request.get_json()
    if ('email' in ConfirmationData and 'code' in ConfirmationData):
        #do something 0..
        user = User.query.filter_by(email=ConfirmationData['email']).first()
        if user.confirmationCode == ConfirmationData['code']:
            # update is confirmed
            user.isConfirmed = 1
            db.session.commit()
            return jsonify("User has been Confirmed thank you !")
        else : 
            return jsonify("Provided Code is not correct please check your email")

        
# PUT /api/users/<user_id> - Update an existing user
@api_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get_or_404(user_id)
    
    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']
    
    db.session.commit()
    return jsonify(user.to_dict())

# DELETE /api/users/<user_id> - Delete a user
@api_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200

@api_bp.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()
    realPassword = user.password
    requestpassword = data['password']
    if requestpassword == realPassword :
        return jsonify({
            'status' : 200,
            'user': user.to_dict(),
        })
    else:
        return jsonify({
            'status' : 401,
            'error': "Invalid Informations" ,
        })
