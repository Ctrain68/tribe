from main import ma
from models.Users import Users

class UsersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)