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

    quotedContentId = Column(BigInteger(),
                             ForeignKey('content.id'),
                             index=True)

    quotedContent = relationship('Content',
                                 foreign_keys=[quotedContentId],
                                 backref='quotedFromAppearances')

    quotedClaimId = *TBW*

    quotedClaim = *TBW*

    quotingContentId = *TBW*

    quotingContent = *TBW*

    quotingClaimId = Column(BigInteger(),
                            ForeignKey('claim.id'),
                            index=True)

    quotingClaim = relationship('Claim',
                                foreign_keys=[quotingClaimId],
                                backref='quotingToAppearances')

    stance = *TBW*


    testifierId = *TBW*

    testifier = *TBW*
