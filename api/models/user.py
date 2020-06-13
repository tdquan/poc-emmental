from sqlalchemy import Column, String
from sqlalchemy_api_handler import ApiHandler

from models.mixins.has_science_feedback_mixin import HasScienceFeedbackMixin
from utils.db import Model

__model__ = 'User'


class User(ApiHandler,
           Model,
           HasScienceFeedbackMixin):
  ''' store user-related details '''

  email       = Column(String, nullable=False, unique=True)
  firstName   = Column(String, nullable=False)
  lastName    = Column(String, nullable=False)
