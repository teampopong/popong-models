# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey, func, Integer, select, Text
from sqlalchemy.orm import column_property

from .meeting import Meeting
from .base import Base


class Statement(Base):
    __tablename__ = 'statement'

    id = Column(Integer, autoincrement=True, primary_key=True)
    meeting_id = Column(ForeignKey('meeting.id'), nullable=False, index=True)
    person_id = Column(ForeignKey('person.id'), index=True)

    sequence = Column(Integer, nullable=False)
    speaker = Column(Text)
    content = Column(Text)

    date = column_property(select([Meeting.date])\
                           .where(Meeting.id==meeting_id), deferred=True)

