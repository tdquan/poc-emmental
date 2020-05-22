import os
from sqlalchemy_api_handler import ApiHandler, logger

import repository.science_feedback.entity_from_row
from utils.airtable import request_airtable_rows


SCIENCE_FEEDBACK_AIRTABLE_BASE_ID = os.environ.get('SCIENCE_FEEDBACK_AIRTABLE_BASE_ID')


NAME_TO_AIRTABLE = {
    'editor': 'Editors',
    'reviewer': 'Reviewers',
    'claim': 'Items for review / reviewed',
    'appearance': 'Appearances',
    'review': 'Reviews / Fact-checks',
}


def entity_from_row_for(name, entity_dict):
    function_name = '{}_from_row'.format(name)
    entity_from_row_function = getattr(repository.science_feedback.entity_from_row, function_name)
    return entity_from_row_function(entity_dict)


def sync_for(name, max_records=None):

    rows = request_airtable_rows(
        SCIENCE_FEEDBACK_AIRTABLE_BASE_ID,
        NAME_TO_AIRTABLE[name],
        max_records=max_records
    )

    entities = []
    for row in rows:
        entity = entity_from_row_for(name, row)
        if entity:
            entities.append(entity)

    ApiHandler.save(*entities)


def sync(max_records=None):
    logger.info('import science feedback data...')
    for name in NAME_TO_AIRTABLE.keys():
        sync_for(name, max_records=max_records)
    logger.info('import science feedback data...Done.')
