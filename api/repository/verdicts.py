from sqlalchemy.sql.expression import and_, or_

from models.user import User
from models.verdict import Verdict
from models.claim import Claim
from models.content import Content
from models.medium import Medium
from models.organization import Organization
from models.verdict_tag import VerdictTag
from models.tag import Tag


def verdict_ts_filter(ts_query):
    return or_(
        *[
            model.__ts_vector__.match(
                ts_query,
                postgresql_regconfig='english'
            )
            for model in [Verdict, Claim, Content, Medium, Organization, User]
        ]
    )


def keep_verdicts_with_keywords_chain(query, keywords_chain):
    # Optionable TBW : make the search also able to find keywords
    # in joined claim, content, media and organization columns
    query = query.outerjoin(Claim) \
                 .outerjoin(Content) \
                 .outerjoin(Medium) \
                 .outerjoin(Organization) \
                 .join(VerdictTag) \
                 .join(Tag) \
                 .join(User)

    ts_queries = ['{}:*'.format(keyword) for keyword in keywords_chain.split(' ')]
    ts_filters = [verdict_ts_filter(ts_query) for ts_query in ts_queries]
    query = query.filter(and_(*ts_filters))
    return query


def keep_verdicts_with_tag(query, tag):
    query = query.join(Tag)
    print('tag is {tag}'.format(tag=tag))
