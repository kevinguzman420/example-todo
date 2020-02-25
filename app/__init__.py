from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secret key"

    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://kevinguzman:kevinguzman@127.0.0.1:3306/todolist"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)

    from . auth import auth_bp
    app.register_blueprint(auth_bp)

    from . public import public_bp
    app.register_blueprint(public_bp)

    return app
    