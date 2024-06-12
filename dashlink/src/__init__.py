from flask import Flask

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # initializing flask extensions
    

    # registering blueprints
    from src.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
