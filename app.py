import os
import logging
from flask import Flask, render_template
from flask_orator import Orator
from flasgger import Swagger
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from api_docs import template

load_dotenv(os.path.join(os.path.expanduser('/Users/sjahn/workspace/sjahn.pythonanywhere.com'), '.env'))

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.config['JSON_SORT_KEYS'] = False
app.config['ORATOR_DATABASES'] = {
    'default': 'mysql',
    'mysql': {
        'driver': 'mysql',
        'host': os.getenv('DB_HOST'),
        'database': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'prefix': '',
        'log_queries': bool(os.getenv('LOG_QUERIES'))
    }
}

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  # Change this!
app.config['JWT_TOKEN_LOCATION'] = ['headers'] # headers', 'cookies', 'query_string', 'json'
app.config['SWAGGER'] = {
    'title': 'sjahn.pythonanywhere.com',
    'uiversion': 3,
    'openapi': '3.0.2'
}

db = Orator(app)
jwt = JWTManager(app)
Swagger(app, template=template)

if bool(os.getenv('IS_DEV')):

    logger = logging.getLogger('orator.connection.queries')
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(elapsed_time)sms %(query)s'
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)

from api import users, banners
from web import (
    auth,
    contents
)

app.register_blueprint(auth.blueprint, url_prefix='/user')
app.register_blueprint(users.blueprint, url_prefix='/api/user')

app.register_blueprint(contents.blueprint, url_prefix='/')
app.register_blueprint(banners.blueprint, url_prefix='/api/banners')


@app.route('/')
def index():
    return render_template('main/index.html')
