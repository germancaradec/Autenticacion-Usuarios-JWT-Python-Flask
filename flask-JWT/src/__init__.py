from flask import Flask
from flask_cors import CORS, logging

# Routes
from .routes import AuthRoutes
from .routes import LanguageRoutes

app = Flask(__name__)
CORS(app)


def init_app(config):
    # Configuration
    app.config.from_object(config)

    CORS(app, resources={r"/*": {"origins": "*"}})

    logging.getLogger('flask_cors').level = logging.DEBUG


    # Blueprints
    app.register_blueprint(AuthRoutes.main, url_prefix='/auth')
    app.register_blueprint(LanguageRoutes.main, url_prefix='/languages')

    return app
