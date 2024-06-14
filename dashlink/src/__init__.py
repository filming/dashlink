from flask import Flask

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

    return app
