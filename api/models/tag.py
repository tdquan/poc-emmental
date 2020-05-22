from sqlalchemy import Column, Integer, String, Text
from sqlalchemy_api_handler import ApiHandler

from utils.db import Model


class Tag(ApiHandler,
          Model):

    evaluationValue = Column(Integer())

    info = *TBW*

    label = *TBW*
