from main import db

class Accounts(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    users = db.relationship("Users", backref="user", uselist=False)

    def __repr__(self):
        return f"<Account {self.email}>"