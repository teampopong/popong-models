# -*- coding: utf-8 -*-

from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text, Unicode

from .base import Base


class BillReview(Base):
    __tablename__ = 'bill_review'

    id = Column(Integer, autoincrement=True, primary_key=True)
    bill_id = Column(String(20), ForeignKey('bill.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    name = Column(Unicode(150), index=True, nullable=False)

    start_date = Column(Date, index=True)
    end_date = Column(Date, index=True)
    data = Column(Text)

