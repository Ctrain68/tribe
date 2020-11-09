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
    from models.Users import Users
    from faker import Faker
    faker = Faker()

    for i in range(20):
        user = Users()
        user.username = faker.name()
        user.fname = faker.first_name()
        user.lname = faker.last_name()
        user.userpass = faker.password()
        user.profile_pic=faker.text()
        user.account_active=faker.boolean()
        user.email= faker.email()
        db.session.add(user)

    db.session.commit()
    print("Tables seeded")