from main import ma
from models.Users import Users
from marshmallow.validate import Length

class UsersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users
    username = ma.String(required=True, validate=Length(min=1))
    fname = ma.String(required=True, validate=Length(min=1))
    lname = ma.String(required=True, validate=Length(min=1))
    # userpass = ma.String(required=True, validate=Length(min=1))
    profile_pic = ma.String(required=False)
    account_active = ma.Boolean(required=True)
    # email = ma.String(required=True, validate=Length(min=1))

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)