import traceback

from flask import current_app as app

from repository.science_feedback import sync
from repository.clean import clean
from repository.science_feedback import sync as sync_science_feedback
from repository.tags import sync as sync_tags


@app.manager.command
def sandbox():
    clean()
    sync_tags()
    sync_science_feedback()

    try:
      sync()
    except Exception as err:
      print('ERROR: {err}:'.format(err=err))
      print('--------')
      traceback.print_exc()
