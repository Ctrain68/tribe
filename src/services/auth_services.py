from models.Accounts import Accounts
from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import abort

def verify_user(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        account_id = get_jwt_identity()

        account = Acconts.query.get(account_id)

        if not user:
            return abort(401, description="Invalid user")

        return function(*args, user=user, **kwargs)

    return wrapper