from sqlalchemy_api_handler import logger

from models.appearance import Appearance
from models.claim import Claim
from models.content import Content
from models.review import Review
from models.user import User
from utils.db import db


def clean():
    ''' Order of deletions matters because of foreign key constraints '''
    logger.info('clean all the database...')
    *TBW*
    logger.info('clean all the database...Done.')
