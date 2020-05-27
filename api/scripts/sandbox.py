from flask import current_app as app


from models.user import User
from repository.clean import clean
from utils.db import db


@app.manager.command
def sandbox():
    clean()

    print('create one user...')
    user = User(email='foo.bar@feedback.news')
    db.session.add(user)
    try:
      db.session.commit()
      print('create one user...Done.')
    except Exception as e:
      print(e)
      db.session.rollback()
      db.session.flush()
