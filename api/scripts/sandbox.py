import traceback

from flask import current_app as app
from sqlalchemy_api_handler import logger

from repository.clean import clean
from repository.science_feedback import sync as sync_science_feedback
from repository.tags import sync as sync_tags


@app.manager.command
def sandbox():
    try:
      clean()
      sync_tags()
      sync_science_feedback()
    except Exception as err:
      logger.error('{err}:'.format(err=err))
      print('--------')
      traceback.print_exc()
