from flask import Blueprint, request, jsonify, abort
from schemas.UsersSchema import user_schema, users_schema
from models.Users import Users
from main import db

users = Blueprint("users", __name__, url_prefix="/users")

@users.route("/", methods=["GET"])
def users_index():
    users = Users.query.all()
    return jsonify(users_schema.dump(users))
   

@users.route("/", methods=["POST"])
def users_create():
    
    users_fields = user_schema.load(request.json)

    new_user = Users()
    new_user.username = users_fields["username"]
    new_user.fname = users_fields["fname"]
    new_user.lname = users_fields["lname"]
    new_user.userpass = users_fields["userpass"]
    new_user.profile_pic=users_fields["profile_pic"]
    new_user.account_active=users_fields["account_active"]
    new_user.email= users_fields["email"]
    
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify(user_schema.dump(new_user))

@users.route("/<email>", methods=["GET"])
def users_show(email):
    #Return a single user
    user = Users.query.filter_by(email = email).first()
    return jsonify(user_schema.dump(user))

@users.route("/<int:userid>", methods=["PUT", "PATCH"])
def user_update(userid):
    #Update a user
    user = Users.query.filter_by(userid=userid)
    users_fields = user_schema.load(request.json)
    user.update(users_fields)


    db.session.commit()

    return jsonify(user_schema.dump(user[0]))

@users.route("/<int:userid>", methods=["DELETE"])
def user_delete(userid):
    #Delete a User
    users = Users.query.get(userid = userid)
    db.session.delete(users)
    db.session.commit()

    return jsonify(user_schema.dump(users))