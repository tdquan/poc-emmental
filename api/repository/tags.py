from sqlalchemy_api_handler import ApiHandler, logger

from domain.tags import TAGS
from models.tag import Tag


def sync():
    logger.info('import tags data...')
    ApiHandler.save(*[Tag(**tag) for tag in TAGS])
    logger.info('import tags data...Done')
