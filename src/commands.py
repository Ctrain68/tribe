from main import db
from flask import Blueprint

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables deleted")

@db_commands.cli.command("seed")
def seed_db():
    from models.Accounts import Accounts
    from models.Users import Users
    from faker import Faker
    from main import bcrypt
    import random

    faker = Faker()
    accounts = []

    for i in range(10):
        account = Accounts()
        account.email = f"test{i}@test.com"
        account.password = bcrypt.generate_password_hash("123456").decode("utf-8")
        db.session.add(account)
        accounts.append(account)
        

    for i in range(10):
        user = Users()
        user.username = faker.name()
        user.fname = faker.first_name()
        user.lname = faker.last_name()
        user.profile_pic=faker.text()
        user.account_active=faker.boolean()
        user.account_id = i+1
        db.session.add(user)

    db.session.commit()
    print("Tables seeded")