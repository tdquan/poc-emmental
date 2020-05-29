from sqlalchemy import BigInteger, Column, String
from sqlalchemy_api_handler import ApiHandler

from models.mixins.has_science_feedback_mixin import HasScienceFeedbackMixin
from utils.db import Model


class User(ApiHandler,
           Model,
           HasScienceFeedbackMixin):
  ''' store user-related details '''
  __tablename__ = 'user'

  id          = Column(BigInteger, primary_key=True, autoincrement=True)
  email       = Column(String, nullable=False, unique=False)
  firstName   = Column(String, nullable=False, unique=False)
  lastName    = Column(String, nullable=False, unique=False)

  def __init__(self, email, firstName, lastName):
    self.email = email
    self.firstName = firstName
    self.lastName = lastName

  @property
  def __repr__(self):
    return '<User {id}>'.format(id=self.id)
