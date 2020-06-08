from sqlalchemy_api_handler import logger

from models.appearance import Appearance
from models.claim import Claim
from models.content import Content
from models.review import Reviewt
from models.user import User
from utils.db import db


def clean():
    ''' Order of deletions matters because of foreign key constraints '''
    logger.info('clean all the database...')
    for table in reversed(db.metadata.sorted_tables):
      print("Clearing table {table_name}...".format(table_name=table))
      db.session.execute(table.delete())

    db.session.commit()
    logger.info('clean all the database...Done.')
