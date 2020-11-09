from main import db

class Users(db.Model):
    __tablename__ = 'users'

    userid =db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(), nullable=False)
    lname = db.Column(db.String(), nullable=False)
    userpass = db.Column(db.String(), nullable=False)
    profile_pic = db.Column(db.String())
    account_active = db.Column(db.Boolean())
    email = db.Column(db.String(), nullable=False)
    