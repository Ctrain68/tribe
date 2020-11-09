import os
from dotenv import load_dotenv

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.environ.get("DB_URI")

        if not value:
            raise ValueError("DB_URI is not set")
        return value
        # DB_URI=postgresql+psycopg2://tribe_app:{os.getenv('db_pass')}@localhost:5432/tribe_api
        

class DevelopmentConfig(Config):
    DEBUG= True 

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    TESTING = True 

environment = os.environ.get("FLASK_ENV")

if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()
