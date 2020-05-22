# pylint: disable=C0415
# pylint: disable=W0611

from utils.db import db


def import_models(with_creation=False):
    from models.user import User

    if with_creation:
        db.create_all()
        db.session.commit()
