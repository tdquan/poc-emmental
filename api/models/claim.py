from sqlalchemy import Column, Text
from sqlalchemy_api_handler import ApiHandler

from models.mixins.has_science_feedback_mixin import HasScienceFeedbackMixin
from utils.db import Model

__model__ = 'Claim'


class Claim(ApiHandler,
            Model,
            HasScienceFeedbackMixin):

    text = Column(Text, nullable=False)
