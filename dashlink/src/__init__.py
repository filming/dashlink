from flask import Flask

from os import path

from config import Config
from src.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # initializing flask extensions
    db.init_app(app)

    # registering blueprints
    from src.main import bp as main_bp
    app.register_blueprint(main_bp)

    from src.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    # setting up database
    from src.models.user import User

    create_database(app)

    return app

def create_database(app):
    if not path.exists(f"src/dashlink.db"):
        with app.app_context():
            db.create_all()
            print ("Created database!")
