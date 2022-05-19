from flask_jwt_extended import create_access_token, create_refresh_token
from constants import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from flask import request, jsonify, auth
import validators
from werkzeug.security import check_password_hash, generate_password_hash


#connecttoDB

@auth.post('/register')
def register():
    email = request.get('email')
    password = request.get('password')

    if not validators.email(email):
        return jsonify({'error': "Email is not valid"}), HTTP_400_BAD_REQUEST

    if User.query.filter_by(email=email).first() is not None:
        return jsonify({'error': "Email is taken"}), HTTP_400_BAD_REQUEST
    
    if User.query.filter_by(password=password).first() is not None:
        pwd_hash = generate_password_hash(password)

        user = User(username=username, password=pwd_hash, email=email)
        db.session.add(user)
        db.session.commit()

        return jsonify({
            'message': "User created",
            'user': {
                "id": someid
                "email": email
            }

        }), HTTP_201_CREATED
    else:
        return jsonify({"error": "Недостаточно прав"})

@auth.post('/log_in')
def login():
    email = request.json.get('email', '')
    password = request.json.get('password', '')
    user = user.query.filter_by(email=email).first()

    if user:
        is_pass_correct = check_password_hash(user.password, password)

        if is_pass_correct:
            refresh = create_refresh_token(identity=user.id)
            access = create_access_token(identity=user.id)

            return jsonify({
                'user': {
                    'refresh': refresh,
                    'access': access,
                    'username': user.username,
                    'email': user.email
                }

            }), HTTP_200_OK

    return jsonify({'error': HTTP_401_UNAUTHORIZED})