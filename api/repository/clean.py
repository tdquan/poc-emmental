from models.user import User
from utils.db import db


def clean():
    ''' Order of deletions matters because of foreign key constraints '''
    print('clean all the database...')
    print('{name} *TBW*'.format(name=__name__))
    print('clean all the database...Done.')
