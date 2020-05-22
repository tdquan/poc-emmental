from sqlalchemy import func, Index, TEXT
from sqlalchemy.sql.expression import cast
from sqlalchemy.sql.functions import coalesce

from models.claim import Claim
from models.content import Content
from models.medium import Medium
from models.organization import Organization
from models.review import Review
from models.user import User


def create_tsvector(*targets):
    exp = targets[0]
    for target in targets[1:]:
        exp += ' ' + target
    return func.to_tsvector('english', exp)


def import_keywords():
    Claim.__ts_vector__ = *TBW*

    Claim.__table_args__ = *TBW*


    Content.__ts_vector__ = *TBW*

    Content.__table_args__ = *TBW*


    Medium.__ts_vector__ = *TBW*

    Medium.__table_args__ = *TBW*


    Organization.__ts_vector__ = *TBW*

    Organization.__table_args__ = *TBW*


    Review.__ts_vector__ = create_tsvector(
        cast(coalesce(Review.comment, ''), TEXT),
    )
    Review.__table_args__ = (
        Index(
            'idx_review_fts',
            Review.__ts_vector__,
            postgresql_using='gin'
        ),
    )


    User.__ts_vector__ = *TBW*

    User.__table_args__ = *TBW*
