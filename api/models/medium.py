from sqlalchemy import Column, ForeignKey, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy_api_handler import ApiHandler

from models.mixins.has_science_feedback_mixin import HasScienceFeedbackMixin
from utils.db import Model

__model__ = 'Medium'


class Medium(ApiHandler,
             Model,
             HasScienceFeedbackMixin):

    name           = Column(String(256), nullable=False)

    organizationId = Column(BigInteger, ForeignKey('organization.id'), index=True)

    organization   = relationship('Organization', foreign_keys=[organizationId], backref='media')

    url            = Column(String(300))
