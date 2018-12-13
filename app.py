from flask import Flask
from logging import getLogger

import blueprints
from extensions import cors, deep_detect_extension
from settings import Config

logger = getLogger(__name__)

def create_app(config=Config):
    """Create and set up app."""
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config)

    register_extensions(app)
    register_blueprints(app)

    logger.info(app.config)

    return app

def register_extensions(app):
    """Register extensions."""
    cors.init_app(app, resources={r'/*': {'origins': '*'}})
    deep_detect_extension.init_app(app)


def register_blueprints(app):
    """Register Flask Blueprints."""
    app.register_blueprint(blueprints.products_endpoint, url_prefix='/products')