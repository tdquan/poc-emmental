import os
import traceback
from sqlalchemy_api_handler import ApiHandler, logger

from utils.db import db
from utils.airtable import request_airtable_rows
import repository.science_feedback.entity_from_row
from repository.science_feedback.airtable import sync as sync_airtable
from repository.science_feedback.wordpress import sync as sync_wordpress


def sync(max_records=None):
    sync_airtable(max_records=max_records)
    sync_wordpress()


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

    # ApiHandler.save(*entities)
    try:
        for entity in entities:
            db.session.add(entity)
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        db.session.flush()
        print('ERROR: {err}:'.format(err=err))
        print('--------')
        traceback.print_exc()


# def sync(max_records=None):
#     logger.info('import science feedback data...')
#     for name in NAME_TO_AIRTABLE.keys():
#         sync_for(name, max_records=max_records)
#     logger.info('import science feedback data...Done.')
