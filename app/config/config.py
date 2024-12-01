import os
from pathlib import Path
from dotenv import load_dotenv


basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_DEV_URL")
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args": {
            "options": "-csearch_path=pago_schema"
        }
    }
    CACHE_REDIS_URL = os.getenv('REDIS_URL')


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_TEST_URL")
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args": {
            "options": "-csearch_path=pago_schema"
        }
    }
    CACHE_REDIS_URL = os.getenv('REDIS_URL')

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_RECORD_QUERIES = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_PROD_URL")
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args": {
            "options": "-csearch_path=pago_schema"
        }
    }
    CACHE_REDIS_URL = os.getenv('REDIS_URL')

def factory(app):
    configuation = {
        "development": DevelopmentConfig,
        "testing": TestConfig,
        "production": ProductionConfig,
    }
    return configuation[app]
