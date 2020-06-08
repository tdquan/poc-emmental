from sqlalchemy import Column, String


class HasScienceFeedbackMixin():
    scienceFeedbackIdentifier = Column(String(32))
    scienceFeedbackUrl = Column(String(512))
    scienceFeedbackId = Column(String(32))
