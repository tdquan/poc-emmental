from models.user import User
from utils.db import db


def clean():
    ''' Order of deletions matters because of foreign key constraints '''
    print('clean all the database...')
    for table in reversed(db.metadata.sorted_tables):
      print("Clearing table {table_name}...".format(table_name=table))
      db.session.execute(table.delete())

    db.session.commit()
    print('clean all the database...Done.')
