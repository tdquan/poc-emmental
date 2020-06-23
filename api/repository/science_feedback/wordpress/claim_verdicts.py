from sqlalchemy_api_handler import humanize

from domain.science_feedback.wordpress.claim_review import claim_review_from_url
from models.tag import Tag
from models.verdict import Verdict
from models.verdict_tag import VerdictTag
from utils.asynchronous import map_asynchronous


def claim_verdicts_from_airtable(max_verdicts=None):
    query = Verdict.query.filter(Verdict.scienceFeedbackUrl != None)
    if max_verdicts is not None:
        query = query.limit(max_verdicts)

    verdicts = query.all()

    if max_verdicts is not None:
        max_verdicts = len(verdicts)

    urls = [verdict.scienceFeedbackUrl for verdict in verdicts][:max_verdicts]
    claim_reviews = map_asynchronous(claim_review_from_url, urls)

    for (index, verdict) in enumerate(verdicts):
        claim_review = claim_reviews[index]
        if not claim_review:
            continue

        for conclusion in claim_review['conclusions']:
            tag = Tag.create_or_modify({'label': conclusion}, search_by='label')
            verdict_tag = VerdictTag.create_or_modify({
                'tagId': humanize(tag.id),
                'verdictId': humanize(verdict.id)
            }, search_by=['tagId', 'verdictId'])
            verdict.verdictTags = verdict.verdictTags + [verdict_tag]

    return verdicts
