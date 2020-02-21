from flask import Flask
# from flask_login import LoginManager
# from flask_sqlalchemy import SQLAlchemy


# login_manager = LoginManager()
# db  = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secret key"
    # Modificar a mysql:
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:testing@localhost:5432/miniblog'
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

    # login_manager.init_app(app)
    # login_manager.login_view = "auth.signin"
    
    # db.init_app(app)
    from . auth import auth_bp
    app.register_blueprint(auth_bp)

    from . public import public_bp
    app.register_blueprint(public_bp)
    # Register the blueprints:

    #

    return app