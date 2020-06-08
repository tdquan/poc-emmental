from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import backref, relationship
from sqlalchemy_api_handler import ApiHandler

from utils.db import Model


class VerdictReviewer(ApiHandler,
                      Model):

    verdictId = *TBW*

    verdict = *TBW*

    reviewerId = *TBW*

    reviewer = *TBW*
