from sqlalchemy import BigInteger, \
                       Column, \
                       ForeignKey, \
                       Integer, \
                       Text
from sqlalchemy.orm import relationship
from sqlalchemy.orm.collections import InstrumentedList
from sqlalchemy_api_handler import ApiHandler

from models.mixins.has_science_feedback_mixin import HasScienceFeedbackMixin
from utils.db import Model

__model__ = 'Review'


class Review(ApiHandler,
             Model,
             HasScienceFeedbackMixin):

    claimId       = Column(BigInteger(),
                           ForeignKey('claim.id'),
                           index=True)

    claim         = relationship('Claim',
                                 foreign_keys=[claimId],
                                 backref='reviews')

    contentId     = Column(BigInteger(),
                           ForeignKey('content.id'),
                           index=True)

    content       = relationship('Content',
                                 foreign_keys=[contentId],
                                 backref='reviews')

    comment       = Column(Text())

    evaluation    = Column(Integer())

    reviewerId    = Column(BigInteger(),
                           ForeignKey('user.id'),
                           index=True)

    reviewer      = relationship('User',
                                 foreign_keys=[reviewerId],
                                 backref='reviews')
