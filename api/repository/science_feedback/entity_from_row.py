from models.appearance import Appearance
from models.content import Content
from models.claim import Claim
from models.review import Review
from models.user import User


def appearance_from_row(row):
    reviewed_items = row.get('Item reviewed')
    if not reviewed_items:
        return

    quoting_content_dict = {'url': row['url']}
    quoting_content = Content.create_or_modify(quoting_content_dict, search_by=['url'])

    quoted_claim = Claim.query.filter_by(scienceFeedbackId=reviewed_items[0]).first()
    quoted_content = None
    if not quoted_claim:
        quoted_content = Content.query.filter_by(scienceFeedbackId=reviewed_items[0]).first()
    if not quoted_claim and not quoted_content:
        return

    science_feedback_testifier_ids = row.get('Verified by')
    if not science_feedback_testifier_ids:
        return
    testifier = User.query.filter_by(scienceFeedbackId=science_feedback_testifier_ids[0]).first()
    if not testifier:
        return

    appearance_dict = {
        'quotedClaim': quoted_claim,
        'quotedContent': quoted_content,
        'quotingContent': quoting_content,
        'scienceFeedbackId': row['airtableId'],
        'testifier': testifier
    }

    return Appearance.create_or_modify(appearance_dict, search_by=['scienceFeedbackId'])


def claim_from_row(row):
    text = row.get('Claim checked (or Headline if no main claim)')
    if not text:
        return

    claim_dict = {
        'scienceFeedbackId': row['airtableId'],
        'text': text
    }

    return Claim.create_or_modify(claim_dict, search_by=['scienceFeedbackId'])


def editor_from_row(row):
    first_name, last_name = row['Name'].split(' ')
    user_dict = {
        'email': '{}.{}@feedback.news'.format(first_name.lower(), last_name.lower()),
        'firstName': first_name,
        'lastName': last_name,
        'scienceFeedbackId': row['airtableId']
    }

    user = User.create_or_modify(user_dict, search_by=['scienceFeedbackId'])

    return user


def review_from_row(row):
    science_feedback_reviewer_ids = row.get('Review editor(s)')
    if not science_feedback_reviewer_ids:
        return
    reviewer = User.query.filter_by(scienceFeedbackId=science_feedback_reviewer_ids[0]).first()
    if not reviewer:
        return

    claim = Claim.query.filter_by(scienceFeedbackId=row['Items reviewed'][0]).first()
    if not claim:
        return

    review_dict = {
        'claim': claim,
        'scienceFeedbackId': row['airtableId'],
        'reviewer': reviewer
    }

    return Review.create_or_modify(review_dict, search_by=['scienceFeedbackId'])


def reviewer_from_row(row):
    user_dict = {
        'email': row['Email'],
        'firstName': row['First name'],
        'lastName': row['Last name'],
        'scienceFeedbackId': row['airtableId']
    }

    user = User.create_or_modify(user_dict, search_by=['scienceFeedbackId'])

    return user
