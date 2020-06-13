from flask import current_app as app
from sqlalchemy_api_handler import logger

from utils.db import db
import models


@app.manager.shell
def make_shell_context():
    mods = {}
    for model in models.__all__:
        mods[model.__name__] = model
    logger.info('Starting shell...')
    return ({'app': app, 'db': db, **mods})
