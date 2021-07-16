
"""Flask configuration."""
import os
import dotenv

def init_app(app, env):
    basedir = os.path.abspath(os.path.dirname(__file__))
    dotenv.load_dotenv(os.path.join(basedir, '.env'))

    if env == "test":
        app.config.from_object(os.environ["ENV_TEST"])
        return 
    
    app.config.from_object(os.environ["ENV"])

class Config:
    """Base config."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    API_TITLE = 'Pond5 API'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.2'
    OPENAPI_URL_PREFIX = '/doc'
    OPENAPI_REDOC_PATH = '/redoc'
    OPENAPI_SWAGGER_UI_PATH = '/swagger'
    OPENAPI_SWAGGER_UI_URL = 'https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.19.5/'
    API_SPEC_OPTIONS = {'host': 'localhost:5000/api/v1/', 'x-internal-id': '2'}


class DevConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS=True


class TestingConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI = "sqlite:///testing.db"
    TESTING = True