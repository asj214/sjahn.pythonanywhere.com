from datetime import datetime
from flask import Blueprint, request, jsonify
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import (
    create_access_token,
    jwt_optional,
    jwt_required,
    get_jwt_identity
)
from models import Banner, Attachment
from serializers import BannerSchema, BannersSchema


blueprint = Blueprint('banners', __name__)

@blueprint.route('/', methods=['GET'])
@jwt_optional
@marshal_with(BannersSchema(many=True))
def index():

    page = request.json.get('page', 1)
    per_page = request.json.get('per_page', 20)
    category_id = request.json.get('category_id', 1)

    banners = Banner.where('category_id', category_id)
    banners = banners.with_('user', 'attachment').order_by('id', 'desc').paginate(per_page, page)

    return banners




