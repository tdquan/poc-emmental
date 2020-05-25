# pylint: disable=W0612
# pylint: disable=W0613

import os
from flask_script import Manager

from models import import_models
from routes import import_routes
from scripts import install_scripts
from utils.db import db


def setup(flask_app,
          with_models_creation=False,
          with_scripts_manager=False,
          with_routes=False):

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('POSTGRES_URL')
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['DEBUG'] = True

    db.init_app(flask_app)

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
