import enum
from sqlalchemy import BigInteger, \
                       Column, \
                       Enum, \
                       ForeignKey
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship
from sqlalchemy_api_handler import ApiHandler

from models.mixins.has_science_feedback_mixin import HasScienceFeedbackMixin
from utils.db import Model

__model__ = 'Appearance'


class StanceType(enum.Enum):
    ENDORSEMENT = {
        'label': 'endorsement',
        'value': 1
    }
    NEUTRAL = {
        'label': 'neutral',
        'value': 0
    }
    REFUSAL = {
        'label': 'refusal',
        'value': -1
    }


class Appearance(ApiHandler,
                 Model,
                 HasScienceFeedbackMixin):

    quotedContentId     = Column(BigInteger,
                                 ForeignKey('content.id'),
                                 index=True)

    quotedContent       = relationship('Content',
                                       foreign_keys=[quotedContentId],
                                       backref='quotedFromAppearances')

    quotedClaimId       = Column(BigInteger,
                                 ForeignKey('claim.id'),
                                 index=True)

    quotedClaim         = relationship('Claim',
                                       foreign_keys=[quotedClaimId],
                                       backref='quotedFromAppearances')

    quotingContentId    = Column(BigInteger,
                                 ForeignKey('content.id'),
                                 index=True)

    quotingContent      = relationship('Content',
                                       foreign_keys=[quotedContentId],
                                       backref='quotingToAppearances')

    quotingClaimId      = Column(BigInteger,
                                 ForeignKey('claim.id'),
                                 index=True)

    quotingClaim        = relationship('Claim',
                                       foreign_keys=[quotingClaimId],
                                       backref='quotingToAppearances')

    stance              = Enum(StanceType)

    testifierId         = Column(BigInteger,
                                 ForeignKey('user.id'),
                                 index=True)

    testifier           = relationship('User',
                                       foreign_keys=[testifierId],
                                       backref='appearances')
