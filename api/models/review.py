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


class Review(ApiHandler,
             Model,
             HasScienceFeedbackMixin):

    claimId = Column(BigInteger(),
                     ForeignKey('claim.id'),
                     index=True)

    claim = relationship('Claim',
                         foreign_keys=[claimId],
                         backref='reviews')

    contentId = *TBW*

    content = *TBW*

    comment = *TBW*

    evaluation = *TBW*

    reviewerId = *TBW*

    reviewer = *TBW*
