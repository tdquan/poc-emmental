from sqlalchemy import Column, String


class HasScienceFeedbackMixin():
    scienceFeedbackId = Column(String(32))
