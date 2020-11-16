from models.Accounts import Accounts
from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import abort

def verify_account(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        
        account_id = get_jwt_identity()

        account = Accounts.query.get(account_id)

        if not account:
            return abort(401, description="Invalid user")

        return function(*args, account=account, **kwargs)

    return wrapper