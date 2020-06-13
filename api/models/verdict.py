from sqlalchemy import BigInteger, \
                       Column, \
                       Enum, \
                       ForeignKey, \
                       String
from sqlalchemy.orm import relationship
from sqlalchemy_api_handler import ApiHandler

from models.mixins.has_science_feedback_mixin import HasScienceFeedbackMixin
from utils.db import Model

__model__ = 'Verdict'


class Verdict(ApiHandler,
              Model,
              HasScienceFeedbackMixin):

    claimId = Column(BigInteger(),
                     ForeignKey('claim.id'),
                     nullable=False,
                     index=True)

    claim = relationship('Claim',
                         foreign_keys=[claimId],
                         backref='verdicts')

    contentId = Column(BigInteger(),
                       ForeignKey('content.id'),
                       index=True)

    content = relationship('Content',
                           foreign_keys=[contentId],
                           backref='verdicts')

    editorId = Column(BigInteger(),
                      ForeignKey('user.id'),
                      index=True)

    editor = relationship('User',
                          foreign_keys=[editorId],
                          backref='verdicts')

    title = Column(String(), nullable=False)
