import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest, InternalServerError, UnprocessableEntity
from logging.config import dictConfig

from .api import api_bp
from .common import error_handling as error
from .common.logging import config_logging

# instantiate extensions
db = SQLAlchemy()


def create_app(environment='development'):

    # Set config logging
    dictConfig(config_logging())

    # Instantiate app.
    app = Flask(__name__)

    # Set app config.
    env = os.environ.get('FLASK_ENV', environment)
    app.config.from_pyfile(f'../config/{env}.cfg')

    # Set log level
    app.logger.setLevel(app.config['LOG_LEVEL'])

    # Initializing app.
    app.logger.info('Initializing app')
    db.init_app(app)

    # Register blueprints.
    app.logger.info('Registering blueprints')
    app.register_blueprint(api_bp, url_prefix='')

    # Error handlers.
    app.logger.info('Registering error handlers')
    app.register_error_handler(BadRequest, error.handle_validation_error)
    app.register_error_handler(UnprocessableEntity, error.handle_validation_error)
    app.register_error_handler(InternalServerError, error.handle_internal_error)

    return app
