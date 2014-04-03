from sqlalchemy import Column, func, Integer, select, String, Unicode
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import cast

from .base import Base
from .person import Person

class School(Base):
    __tablename__ = 'school'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Unicode(40), index=True)



person_school = select([func.unnest(Person.education_id).label('school_id'),
                        Person.id.label('person_id')]).alias()


School.alumni = relationship("Person",
            secondary=person_school,
            primaryjoin=cast(School.id, String) == person_school.c.school_id,
            secondaryjoin=person_school.c.person_id == Person.id,
            viewonly=True,
            backref='schools')

