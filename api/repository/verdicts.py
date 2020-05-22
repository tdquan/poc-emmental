from sqlalchemy.sql.expression import and_, or_

from models.user import User
from models.verdict import Verdict


def verdict_ts_filter(ts_query):
    return or_(
        *[
            model.__ts_vector__.match(
                ts_query,
                postgresql_regconfig='english'
            )
            for model in [User, Verdict]
        ]
    )


def keep_verdicts_with_keywords_chain(query, keywords_chain):
    query = query.join(User)
    # Optionable TBW : make the search also able to find keywords
    # in joined claim, content, media and organization columns

    ts_queries = ['{}:*'.format(keyword) for keyword in keywords_chain.split(' ')]
    ts_filters = *TBW*
    query = query.filter(and_(*ts_filters))
    return query
