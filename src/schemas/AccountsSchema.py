from main import ma
from models.Accounts import Accounts
from marshmallow.validate import Length

class AccountsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Accounts
        load_only = ["password"]
    
    email = ma.String(required=True, validate=Length(min=4))
    password = ma.String(required=True, validate=Length(min=6))

account_schema = AccountsSchema()
accounts_schema = AccountsSchema(many=True)