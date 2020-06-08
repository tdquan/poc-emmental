# pylint: disable=C0415
# pylint: disable=W0611

from utils.db import db
from repository.keywords import import_keywords


def import_models(with_creation=False):
    *TBW*
    from models.user import User
    from models.appearance import Appearance
    from models.claim import Claim
    from models.content import Content
    from models.review import Review

    if with_creation:
        db.create_all()
        db.session.commit()

    import_keywords()
