from main import db
from sqlalchemy.orm import backref
from models.User import Users

class Tribe(db.Model):
    __tablename__ ='tribes'

    id = db.Column(db.Integer, primary_key=True)
    tribename = db.Column(db.String(), nullable=False, unique=True)