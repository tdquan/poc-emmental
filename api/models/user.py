from sqlalchemy import BigInteger, Column, String

from utils.db import Model


class User(Model):
  ''' store user-related details '''
  id = Column(BigInteger, primary_key=True, autoincrement=True)
  email = Column(String, nullable=False, unique=False)
