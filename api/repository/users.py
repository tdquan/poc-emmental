from sqlalchemy import and_
from sqlalchemy_api_handler import ApiErrors, ApiHandler, logger

from models.user import User


def create_poctest_user():
    logger.info('create poctest user...')
    user = User(
        firstName='Test',
        lastName='User',
        email='poctest.user@feedback.news'
    )
    user.set_password('user@AZERTY123')
    ApiHandler.save(user)
    logger.info('create poctest user...Done.')


def get_user_with_credentials(identifier, password):
    errors = ApiErrors()
    errors.status_code = 401

    if identifier is None:
        errors.add_error('identifier', 'Identifier is missing.')
    if password is None:
        errors.add_error('password', 'Password is missing.')
    errors.maybe_raise()

    user = User.query.filter_by(email=identifier).first()

    if not user:
        errors.add_error('identifier', 'Wrong identifier')
        raise errors
    if not user.check_password(password):
        errors.add_error('password', 'Wrong password')
        raise errors

    return user
