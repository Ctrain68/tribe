from flask import Blueprint
from schemas.AccountsSchema import account_schema, accounts_schema
from flask import Blueprint, request, jsonify, abort
from models.Accounts import Accounts
from main import bcrypt, db
from flask_jwt_extended import create_access_token
from datetime import timedelta

auth = Blueprint('auth', __name__, url_prefix="/auth")

@auth.route("/register", methods=["POST"])
def auth_register():
    account_fields = account_schema.load(request.json)

    account = Accounts.query.filter_by(email=account_fields["email"]).first()

    if account:
        return abort(400, description="Account already")
    
    account = Accounts()
    account.email = account_fields["email"]
    account.password = bcrypt.generate_password_hash(account_fields["password"]).decode("utf-8")

    db.session.add(account)
    db.session.commit()

    return jsonify(account_schema.dump(account))


@auth.route("/login", methods=["POST"])
def auth_login():
    account_fields = account_schema.load(request.json)

    account = Accounts.query.filter_by(email=account_fields["email"]).first()

    if not account or not bcrypt.check_password_hash(account.password, account_fields["password"]):
        return abort(401, description="Incorrect username and password")

    expiry = timedelta(days=1)
    access_token = create_access_token(identity=str(account.id), expires_delta=expiry)

    return jsonify({ "token": access_token })