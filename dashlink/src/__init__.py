from flask import Flask
from flask_login import LoginManager

from os import path

from config import Config
from src.extensions import db, migrate

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # initializing flask extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # registering blueprints
    from src.main import bp as main_bp
    app.register_blueprint(main_bp)

    from src.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    # setting up database
    from src.models.user import User
    from src.models.link import Link

    create_database(app)

    # setting up login manager
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists(f"src/dashlink.db"):
        with app.app_context():
            db.create_all()
            print ("Created database!")
