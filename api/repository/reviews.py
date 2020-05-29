from sqlalchemy.sql.expression import and_, or_

from models.claim import Claim
from models.content import Content
from models.review import Review
from models.user import User


def review_ts_filter(ts_query):
    return or_(
        *[
            model.__ts_vector__.match(
                ts_query,
                postgresql_regconfig='english'
            )
            for model in [Review, Claim, Content, User]
        ]
    )


def reviews_query_from_keywords_chain(query, keywords_chain):
    query = query.outerjoin(Claim) \
                 .outerjoin(Content) \
                 .join(User)

    ts_queries = ['{}:*'.format(keyword) for keyword in keywords_chain.split(' ')]
    ts_filters = '*TBW*'
    query = query.filter(and_(*ts_filters))
    return query
