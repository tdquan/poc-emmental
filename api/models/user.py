from sqlalchemy import Column, String
from sqlalchemy_api_handler import ApiHandler

from models.mixins.has_science_feedback_mixin import HasScienceFeedbackMixin
from utils.db import Model


class User(ApiHandler,
           Model,
           HasScienceFeedbackMixin):
  ''' store user-related details '''
  __tablename__ = 'user'

  email       = Column(String, nullable=False, unique=False)
  firstName   = Column(String, nullable=False, unique=False)
  lastName    = Column(String, nullable=False, unique=False)
