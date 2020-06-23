from repository.science_feedback.airtable import sync as sync_airtable
from repository.science_feedback.wordpress import sync as sync_wordpress


def sync(max_records=None):
    sync_airtable(max_records=max_records)
    sync_wordpress()
