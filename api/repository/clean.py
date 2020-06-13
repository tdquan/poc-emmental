from sqlalchemy_api_handler import logger
from models import import_models

from utils.db import db


def clean():
    ''' Order of deletions matters because of foreign key constraints '''
    import_models()
    logger.info('clean all the database...')
    for table in reversed(db.metadata.sorted_tables):
      logger.info("Clearing table {table_name}...".format(table_name=table))
      db.session.execute(table.delete())

    db.session.commit()
    logger.info('clean all the database...Done.')
