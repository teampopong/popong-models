from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table

from .api_model import ApiModel
from .base import Base


class Cosponsorship(Base, ApiModel):
    __tablename__ = 'cosponsorship'
    __kind_single__ = 'cosponsorship'
    __kind_list__ = 'cosponsorships'

    id = Column(Integer, autoincrement=True, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'), nullable=False)
    bill_id = Column(String(20), ForeignKey('bill.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    is_sponsor = Column(Boolean, default=False, index=True)
