from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import backref, relationship
from sqlalchemy_api_handler import ApiHandler

from utils.db import Model

__model__ = 'VerdictTag'


class VerdictTag(ApiHandler,
                 Model):

    verdictId = Column(BigInteger(), ForeignKey('verdict.id'), primary_key=True)

    verdict = relationship('Verdict', foreign_keys=[verdictId], backref='verdictTags')

    tagId = Column(BigInteger(), ForeignKey('tag.id'), nullable=False, index=True)

    tag = relationship('Tag', foreign_keys=[tagId], backref='verdictTags')
