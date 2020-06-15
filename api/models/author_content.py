from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import backref, relationship
from sqlalchemy_api_handler import ApiHandler

from utils.db import Model

__model__ = 'AuthorContent'


class AuthorContent(ApiHandler,
                    Model):

    authorId = Column(BigInteger,
                      ForeignKey('user.id'),
                      primary_key=True)

    author = relationship('User',
                          backref=backref('authorContents'),
                          foreign_keys=[authorId])

    contentId = Column(BigInteger, ForeignKey('content.id'), index=True)

    content = relationship('Content', foreign_keys=[contentId], backref='authorContents')
