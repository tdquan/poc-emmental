# pylint: disable=W0612
# pylint: disable=W0613

import os
from flask_cors import CORS
from flask_script import Manager
from sqlalchemy_api_handler import ApiHandler, logger

from models import import_models
from routes import import_routes
from scripts import install_scripts
from utils.db import db


def setup(flask_app,
          with_cors=False,
          with_models_creation=False,
          with_scripts_manager=False,
          with_routes=False):

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('POSTGRES_URL')
    flask_app.config['ENV'] = os.environ.get('FLASK_ENV') or 'development'
    flask_app.config['PORT'] = os.environ.get('PORT')
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = flask_app.config['ENV'] == 'production'

    db.init_app(flask_app)
    ApiHandler.set_db(db)

    @flask_app.teardown_request
    def remove_db_session(exc):
        try:
            db.session.remove()
        except AttributeError:
            logger.error('AttributeError: {exc} at {file}'.format(exc=exc, file=__name__))

    if with_cors:
        CORS(flask_app, resources={r'/*': {'origins': 'http://localhost:3000'}}, supports_credentials=True)

    flask_app.app_context().push()

    import_models(with_creation=with_models_creation)

    if with_routes:
        import_routes()

    if with_scripts_manager:
        def create_app(env=None):
            flask_app.env = env
            return flask_app
        flask_app.manager = Manager(create_app)
        install_scripts()
