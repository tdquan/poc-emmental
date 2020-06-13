import enum
from sqlalchemy import Column, Enum, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_api_handler import ApiHandler

from models.mixins.has_science_feedback_mixin import HasScienceFeedbackMixin
from utils.db import Model

__model__ = 'Content'


class ContentType(enum.Enum):
    article = 'article'
    post    = 'post'
    video   = 'video'


class Content(ApiHandler,
              Model,
              HasScienceFeedbackMixin):

    mediumId  = Column(BigInteger, ForeignKey('medium.id'), index=True)
    medium    = relationship('Medium', foreign_keys=[mediumId], backref='contents')
    title     = Column(String(256))
    url       = Column(String, nullable=False)
    type      = Enum(ContentType)
