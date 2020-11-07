from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://tribe_app:{os.getenv('db_pass')}@localhost:5432/tribe_api"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    return db  