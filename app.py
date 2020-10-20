import os
import logging
from flask import Flask
from flask_orator import Orator
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv


load_dotenv(verbose=True)

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

db = Orator(app)
jwt = JWTManager(app)

if bool(os.getenv('IS_DEV')):

    logger = logging.getLogger('orator.connection.queries')
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(elapsed_time)sms %(query)s'
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)


@app.route('/')
def index():
    return os.getenv('DB_HOST')
