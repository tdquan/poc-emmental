import traceback

from flask import current_app as app
from sqlalchemy_api_handler import logger

from repository.clean import clean
from repository.science_feedback import sync as sync_science_feedback
from repository.tags import sync as sync_tags
from repository.users import create_poctest_user


@app.manager.command
def sandbox():
    try:
        clean()
        sync_tags()
        sync_science_feedback()
        create_poctest_user()
    except Exception as err:
        logger.error('{err}:'.format(err=err))
        print('--------')
        traceback.print_exc()
