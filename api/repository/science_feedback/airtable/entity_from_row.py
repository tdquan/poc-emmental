from sqlalchemy_api_handler import humanize

from models.appearance import Appearance
from models.author_content import AuthorContent
from models.content import Content
from models.claim import Claim
from models.medium import Medium
from models.organization import Organization
from models.user import User
from models.verdict import Verdict
from utils.token import create_random_password


def appearance_from_row(row):
    reviewed_items = row.get('Item reviewed')
    if not reviewed_items:
        return

    quoting_content_dict = {'url': row['url'].strip()}
    quoting_content = Content.create_or_modify(quoting_content_dict, search_by='url')
    medium_science_feedback_ids = row.get('Outlet')
    if medium_science_feedback_ids:
        medium = Medium.query.filter_by(scienceFeedbackIdentifier=medium_science_feedback_ids[0]).first()
        quoting_content.mediumId = medium.id

    author_science_feedback_ids = row.get('Authors')
    if author_science_feedback_ids:
        for author_science_feedback_id in author_science_feedback_ids:
            author = User.query.filter_by(scienceFeedbackIdentifier=author_science_feedback_id).first()
            author_content = AuthorContent.create_or_modify({
                'authorId': humanize(author.id),
                'contentId': humanize(quoting_content.id)
            }, search_by=['authorId', 'contentId'])
            quoting_content.authorContents = quoting_content.authorContents + [author_content]

    quoted_claim = Claim.query.filter_by(scienceFeedbackIdentifier=reviewed_items[0]).first()
    quoted_content = None
    if not quoted_claim:
        quoted_content = Content.query.filter_by(scienceFeedbackIdentifier=reviewed_items[0]).first()
    if not quoted_claim and not quoted_content:
        return

    testifier_science_feedback_ids = row.get('Verified by')
    if not testifier_science_feedback_ids:
        return
    testifier = User.query.filter_by(scienceFeedbackIdentifier=testifier_science_feedback_ids[0]).first()
    if not testifier:
        return

    appearance_dict = {
        'quotedClaim': quoted_claim,
        'quotedContent': quoted_content,
        'quotingContent': quoting_content,
        'scienceFeedbackIdentifier': row['airtableId'],
        'testifier': testifier
    }

    return Appearance.create_or_modify(appearance_dict, search_by='scienceFeedbackIdentifier')


def author_from_row(row):
    chunks = row['Name'].split(' ')
    first_name = chunks[0]
    last_name = ' '.join(chunks[1:])
    user_dict = {
        'email': '{}.{}@feedback.news'.format(first_name, last_name),
        'firstName': first_name,
        'lastName': last_name,
        'scienceFeedbackIdentifier': row['airtableId']
    }

    user = User.create_or_modify(user_dict, search_by='email')
    if not user.id:
        user.set_password(create_random_password())

    return user


def claim_from_row(row):
    text = row.get('Claim checked (or Headline if no main claim)')
    if not text:
        return

    claim_dict = {
        'scienceFeedbackIdentifier': row['airtableId'],
        'text': text
    }

    return Claim.create_or_modify(claim_dict, search_by='scienceFeedbackIdentifier')


def editor_from_row(row):
    first_name, last_name = row['Name'].split(' ')
    user_dict = {
        'email': '{}.{}@feedback.news'.format(first_name.lower(), last_name.lower()),
        'firstName': first_name,
        'lastName': last_name,
        'scienceFeedbackIdentifier': row['airtableId']
    }

    user = User.create_or_modify(user_dict, search_by='email')
    if not user.id:
        user.set_password(create_random_password())

    return user


def outlet_from_row(row):
    medium_dict = {
        'name': row['Name'],
        'scienceFeedbackIdentifier': row['airtableId']
    }

    return Medium.create_or_modify(medium_dict, search_by='scienceFeedbackIdentifier')


def reviewer_from_row(row):
    user_dict = {
        'email': row['Email'],
        'firstName': row['First name'],
        'lastName': row['Last name'],
        'scienceFeedbackIdentifier': row['airtableId']
    }

    user = User.create_or_modify(user_dict, search_by='email')
    if not user.id:
        user.set_password(create_random_password())

    return user


def social_from_row(row):
    if 'url' not in row:
        return

    organization_name = row['url'].replace('https://www.', '') \
                                  .split('/')[0] \
                                  .split('.')[0] \
                                  .title()
    organization = Organization.create_or_modify(
        {'name': organization_name},
        search_by='name')

    medium_dict = {
        'name': row['Name'],
        'organization': organization,
        'scienceFeedbackIdentifier': row['airtableId'],
        'url': row['url']
    }

    return Medium.create_or_modify(medium_dict, search_by='scienceFeedbackIdentifier')


def verdict_from_row(row):
    science_feedback_editor_ids = row.get('Review editor(s)')
    if not science_feedback_editor_ids:
        return
    editor = User.query.filter_by(scienceFeedbackIdentifier=science_feedback_editor_ids[0]).first()
    if not editor:
        return

    claim = Claim.query.filter_by(scienceFeedbackIdentifier=row['Items reviewed'][0]).first()
    if not claim:
        return

    verdict_dict = {
        'claim': claim,
        'editor': editor,
        'scienceFeedbackIdentifier': row['airtableId'],
        'scienceFeedbackUrl': row['Review url'],
        'title': row['Review headline']
    }

    return Verdict.create_or_modify(verdict_dict, search_by='scienceFeedbackIdentifier')
