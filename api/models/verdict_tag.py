from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_api_handler import ApiHandler

from utils.db import Model

__model__ = 'VerdictTag'
__tablename__ = 'verdict_tag'


class VerdictTag(ApiHandler,
                 Model):

    verdictId   = Column(BigInteger, ForeignKey('verdict.id'), index=True)

    verdict     = relationship('Verdict', foreign_keys=[verdictId], backref='verdictTags')

    tagId       = Column(BigInteger, ForeignKey('tag.id'), nullable=False, index=True)

    tag         = relationship('Tag', foreign_keys=[tagId], backref='verdictTags')
