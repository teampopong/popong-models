from base import Base
import assembly
import bill
import bill_keyword
import bill_review
import bill_status
import bill_withdrawal
import candidacy
import cosponsorship
import election
import keyword
import meeting
import meeting_attendee
import party
import person
import pledge
import region
import school
import statement

# import all models
for model in Base.__subclasses__():
    globals()[model.__name__] = model

