from flask import current_app as app


from models.user import User
from repository.clean import clean
from utils.db import db


@app.manager.command
def sandbox():
    clean()

    print('create one user...')
    print('{name} *TBW*'.format(name=__name__))
    print('create one user...Done.')
