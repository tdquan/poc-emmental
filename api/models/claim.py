from sqlalchemy import Column, Text
from sqlalchemy_api_handler import ApiHandler

from models.mixins.has_science_feedback_mixin import HasScienceFeedbackMixin
from utils.db import Model


class Claim(ApiHandler,
            Model,
            HasScienceFeedbackMixin):

    text = *TBW*
