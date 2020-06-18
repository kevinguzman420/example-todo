from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secret key"

    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://user_name:pass_name@host:port/database_name"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    login_manager.init_app(app)
    login_manager.login_view = "auth.signin"
    db.init_app(app)

    from . auth import auth_bp
    app.register_blueprint(auth_bp)

    from . public import public_bp
    app.register_blueprint(public_bp)

    return app
    
