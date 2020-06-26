import bcrypt
from sqlalchemy import Column, LargeBinary, String
from sqlalchemy_api_handler import ApiHandler

from models.mixins.has_science_feedback_mixin import HasScienceFeedbackMixin
from utils.db import Model

__model__ = 'User'


class User(ApiHandler,
           Model,
           HasScienceFeedbackMixin):
    ''' store user-related details '''

    clearTextPassword   = None
    email               = Column(String, nullable=False, unique=True)
    firstName           = Column(String, nullable=False)
    lastName            = Column(String, nullable=False)
    password            = Column(LargeBinary(60), nullable=False)

    def check_password(self, passwordToCheck):
        return bcrypt.checkpw(passwordToCheck.encode('utf8'), self.password)

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def set_password(self, newpass):
        self.clearTextPassword = newpass
        self.password = bcrypt.hashpw(newpass.encode('utf8'), bcrypt.gensalt())
