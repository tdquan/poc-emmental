from flask import current_app as app

from repository.clean import clean as clean_database


@app.manager.command
def clean():
    clean_database()
