from sqlalchemy_api_handler import logger

from utils.db import db


def clean():
    ''' Order of deletions matters because of foreign key constraints '''
    logger.info('clean all the database...')
    *TBW*
    logger.info('clean all the database...Done.')
