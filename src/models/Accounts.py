from main import db
from sqlalchemy.orm import backref
from models.Users import Users

class Accounts(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    users = db.relationship("Users", backref=backref("accounts", uselist=False))

    def __repr__(self):
        return f"<Account {self.email}>"