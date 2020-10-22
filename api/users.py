from datetime import datetime
from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    jwt_optional,
    jwt_required,
    get_jwt_identity
)
from flask_request_validator import (
    PATH,
    JSON,
    Param,
    validate_params
)
from werkzeug.security import generate_password_hash, check_password_hash
from models import User


blueprint = Blueprint('users', __name__)

@blueprint.route('/login', methods=['POST'])
@validate_params(
    Param('email', JSON, str, required=True),
    Param('password', JSON, str, required=True),
)
def login(email, password):

    user = User.where('email', email).first()

    if user is not None and check_password_hash(user.password, password):
        user.update(last_login_at=datetime.now())
        token = create_access_token(identity=user.id)
        return jsonify({'status': 200, 'access_token': token})

    return jsonify({'status': 200, 'email': email})