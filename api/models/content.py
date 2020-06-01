import enum
from sqlalchemy import Column, Enum, String
from sqlalchemy_api_handler import ApiHandler

from models.mixins.has_science_feedback_mixin import HasScienceFeedbackMixin
from utils.db import Model


class ContentType(enum.Enum):
    article = 'article'
    post    = 'post'
    video   = 'video'


class Content(ApiHandler,
              Model,
              HasScienceFeedbackMixin):

    title   = Column(String)
    url     = Column(String, nullable=False)
    type    = Enum(ContentType)

    def __repr__(self):
        return '<Content: {id}>'.format(id=self.id)
