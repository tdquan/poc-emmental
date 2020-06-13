from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import backref, relationship
from sqlalchemy_api_handler import ApiHandler

from utils.db import Model

__model__ = 'VerdictReviewer'


class VerdictReviewer(ApiHandler,
                      Model):

    verdictId = Column(BigInteger(), ForeignKey('verdict.id'), primary_key=True)

    verdict = relationship('Verdict', foreign_keys=[verdictId], backref='verdictReviewers')

    reviewerId = Column(BigInteger(), ForeignKey('user.id'), index=True)

    reviewer = relationship('User', foreign_keys=[reviewerId], backref='verdictReviewers')
