import traceback

from flask import current_app as app

from repository.science_feedback import sync
from repository.clean import clean
from utils.db import db


@app.manager.command
def sandbox():
    clean()

    try:
      sync()
    except Exception as err:
      print('ERROR: {err}:'.format(err=err))
      print('--------')
      traceback.print_exc()
