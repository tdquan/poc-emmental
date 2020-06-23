from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import backref, relationship
from sqlalchemy_api_handler import ApiHandler

from utils.db import Model


class VerdictTag(ApiHandler,
                 Model):

    verdictId = *TBW*

    verdict = *TBW*

    tagId = *TBW*

    tag = *TBW*
