from sqlalchemy import BigInteger, Column, String

from utils.db import Model


class User(Model):
  ''' store user-related details '''
  __tablename__ = 'user'

  id      = Column(BigInteger, primary_key=True, autoincrement=True)
  email   = Column(String, nullable=False, unique=False)

  def __init__(self, email):
    self.email = email

  def __repr__(self):
    return '<User {id}'.format(id=self.id)
