import bcrypt
from sqlalchemy import Column, LargeBinary, String
from sqlalchemy_api_handler import ApiHandler

from models.mixins.has_science_feedback_mixin import HasScienceFeedbackMixin
from utils.db import Model


class User(ApiHandler,
           Model,
           HasScienceFeedbackMixin):

    clearTextPassword = None

    email = *TBW*

    firstName = *TBW*

    lastName = *TBW*

    password = Column(LargeBinary(60), nullable=False)

    def check_password(self, passwordToCheck):
        return *TBW*

    def get_id(self):
        return *TBW*

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def set_password(self, newpass):
        self.clearTextPassword = newpass
        self.password = bcrypt.hashpw(*TBW*, *TBW*)
