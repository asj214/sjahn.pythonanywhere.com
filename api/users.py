from datetime import datetime
from flask import Blueprint, request, jsonify
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import (
    create_access_token,
    jwt_optional,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from serializers import CreateUserSchema, LoginSchema, UserSchema


blueprint = Blueprint('users', __name__)

@blueprint.route('/', methods=['POST'])
@jwt_optional
@use_kwargs(CreateUserSchema())
@marshal_with(UserSchema())
def create(email, name, password, **kwargs):

    if User.where('email', email).first() is None:
        user = User()
        user.email = email
        user.name = name
        user.password = generate_password_hash(password)
        user.save()
        return user
    else:
        return jsonify({'status': 500, 'message': 'email has exists'})


@blueprint.route('/', methods=['GET'])
@jwt_required
@marshal_with(UserSchema())
def show():

    id = get_jwt_identity()

    user = User.find(id)
    return user


@blueprint.route('/login', methods=['POST'])
@jwt_optional
@use_kwargs(LoginSchema())
@marshal_with(LoginSchema())
def login(email, password, **kwargs):

    user = User.where('email', email).first()

    if user is not None and check_password_hash(user.password, password):
        user.update(last_login_at=datetime.now())
        token = create_access_token(identity=user.id)
        return jsonify({'status': 200, 'access_token': token})

    return jsonify({'status': 404, 'message': 'not found your email'})