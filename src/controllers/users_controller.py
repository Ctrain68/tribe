from flask import Blueprint, request, jsonify, abort
from schemas.UsersSchema import user_schema, users_schema
from models.Users import Users
from models.Accounts import Accounts
from flask_jwt_extended import jwt_required, get_jwt_identity
from main import db

users = Blueprint("users", __name__, url_prefix="/users")

@users.route("/", methods=["GET"])
def users_index():
    users = Users.query.all()
    return jsonify(users_schema.dump(users))
   

@users.route("/", methods=["POST"])
@jwt_required
def users_create():
    
    users_fields = user_schema.load(request.json)
    account_id = get_jwt_identity()

    account = Accounts.query.get(account_id)

    if not account:
        return abort(401, description="Account not found")

    user = Users.query.get(account_id)

    if not user:
    
        new_user = Users()
        new_user.username = users_fields["username"]
        new_user.fname = users_fields["fname"]
        new_user.lname = users_fields["lname"]
        new_user.profile_pic=users_fields["profile_pic"]
        new_user.account_active=users_fields["account_active"]
        
        account.users.append(new_user)
        
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify(user_schema.dump(new_user))
    
    else:
        return abort(401, description='User Profile already exists')

@users.route("/<string:username>", methods=["GET"])

def users_show(username):
    #Return a single user
    user = Users.query.filter_by(username = username).first()
    return jsonify(user_schema.dump(user))

@users.route("/<string:username>", methods=["PUT", "PATCH"])
@jwt_required
def user_update(username):

    users_fields = user_schema.load(request.json)
    account_id = get_jwt_identity()

    account = Accounts.query.get(account_id)

    if not account:
        return abort(401, description="Account not found")
    #Update a user
    user = Users.query.filter_by(username = username)
    users_fields = user_schema.load(request.json)
    user.update(users_fields)


    db.session.commit()

    return jsonify(user_schema.dump(user[0]))

@users.route("/<string:username>", methods=["DELETE"])
@jwt_required
def user_delete(username):

    users_fields = user_schema.load(request.json)
    account_id = get_jwt_identity()

    account = Accounts.query.get(account_id)

    if not account:
        return abort(401, description="Account not found")
    #Delete a User
    users = Users.query.filter_by(username=username)
    db.session.delete(users)
    db.session.commit()

    return jsonify(user_schema.dump(users))