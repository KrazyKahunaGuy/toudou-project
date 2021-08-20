import os
from dotenv import load_dotenv


BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

class Config:
    FLASK_DEBUG = os.environ['FLASK_DEBUG'] or True
    FLASK_ENV = os.environ['FLASK_ENV'] or 'development'
    CSRF_ENABLED = os.environ['CSRF_ENABLED'] or True
    SECRET_KEY = os.environ['SECRET_KEY'] or 'i-am-a-secret'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] or 'postgresql:///toudou_dev'
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ['SQLALCHEMY_TRACK_MODIFICATIONS'] or True
