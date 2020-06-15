from sqlalchemy import Column, String
from sqlalchemy_api_handler import ApiHandler

from models.mixins.has_science_feedback_mixin import HasScienceFeedbackMixin
from utils.db import Model

__model__ = 'Organization'


class Organization(ApiHandler,
                   Model,
                   HasScienceFeedbackMixin):

    name  = Column(String(256), nullable=False)
