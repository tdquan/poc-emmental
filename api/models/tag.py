from sqlalchemy import Column, Integer, String, Text
from sqlalchemy_api_handler import ApiHandler

from utils.db import Model

__model__ = 'Tag'


class Tag(ApiHandler,
          Model):

    evaluationValue = Column(Integer())

    info = Column(Text())

    label = Column(String(256), nullable=False)
