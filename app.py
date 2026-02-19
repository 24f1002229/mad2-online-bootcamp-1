from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore
from backend.models import db, User, Role 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_database"
datastore = SQLAlchemyUserDatastore(db, User, Role)
app.security = Security(app, datastore)


with app.app_context():
    db.init_app(app)
    db.create_all()

    app.security.datastore.find_or_create_role(name="admin", description="superuser")
    app.security.datastore.find_or_create_role(name="user", description="general_user")
    if not app.security.datastore.find_user(email="admin@gmail.com"):
        app.security.datastore.create_user(
            email = "admin@gmail.com",
            username="admin",
            password="1234",
            roles=["admin"]
        )

    if not app.security.datastore.find_user(email="user@gmail.com"):
        app.security.datastore.create_user(
            email="user@gmail.com",
            username="user",
            password="1234",
            roles=["user"]
        )

    db.session.commit()


from backend.routes import *


if __name__ == "__main__":
    app.run(debug=True)