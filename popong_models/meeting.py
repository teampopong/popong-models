# -*- coding: utf-8 -*-

from sqlalchemy import BigInteger, Column, Date, ForeignKey, Text
from sqlalchemy.dialects.postgresql import ARRAY, JSON
from sqlalchemy.orm import deferred, relationship

from .base import Base
from .meeting_attendee import MeetingAttendee


class Meeting(Base):
    __tablename__ = 'meeting'

    # Identifiers
    id = Column(BigInteger, primary_key=True)
    committee = Column(Text, index=True)
    region_id = Column(ForeignKey('region.id'), index=True)
    parliament_id = Column(Text, nullable=False, index=True)
    session_id = Column(Text, index=True)
    sitting_id = Column(Text, index=True)

    # Meta & contents
    date = Column(Date, nullable=False, index=True)
    issues = deferred(Column(ARRAY(Text)), group='extra')
    dialogue = deferred(Column(JSON), group='extra')
    url = deferred(Column(Text), group='extra')
    pdf_url = deferred(Column(Text), group='extra')

    attendees = relationship('Person',
            secondary=MeetingAttendee.__table__,
            backref='meeting')

    statements = relationship('Statement',
            order_by='Statement.sequence',
            backref='meeting')

