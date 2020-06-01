from sqlalchemy import func, Index, TEXT
from sqlalchemy.sql.expression import cast
from sqlalchemy.sql.functions import coalesce

from models.claim import Claim
from models.content import Content
from models.review import Review
from models.user import User


def create_tsvector(*targets):
    exp = targets[0]
    for target in targets[1:]:
        exp += ' ' + target
    return func.to_tsvector('english', exp)


def import_keywords():
    Claim.__ts_vector__ = create_tsvector(
        cast(coalesce(Claim.text, ''), TEXT),
    )

    Claim.__table_args__ = (
        Index(
            'idx_claim_fts',
            Claim.__ts_vector__,
            postgresql_using='gin'
        ),
    )

    Content.__ts_vector__ = create_tsvector(
        cast(coalesce(Content.title, ''), TEXT),
        cast(coalesce(Content.url, ''), TEXT),
    )

    Content.__table_args__ = (
        Index(
            'idx_content_fts',
            Content.__ts_vector__,
            postgresql_using='gin'
        ),
    )

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

    User.__ts_vector__ = create_tsvector(
        cast(coalesce(User.email, ''), TEXT),
        cast(coalesce(User.firstName, ''), TEXT),
        cast(coalesce(User.lastName, ''), TEXT),
    )

    User.__table_args__ = (
        Index(
            'idx_user_fts',
            Claim.__ts_vector__,
            postgresql_using='gin'
        ),
    )
