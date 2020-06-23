from flask import current_app as app

from repository.clean import clean
from repository.science_feedback import sync as sync_science_feedback
from repository.tags import sync as sync_tags
from repository.users import create_poctest_user


@app.manager.command
def sandbox():
    clean()
    sync_tags()
    sync_science_feedback()
    create_poctest_user()
