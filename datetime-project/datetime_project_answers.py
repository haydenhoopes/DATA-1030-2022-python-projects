# Name:
# BTECH #:

# Import the datetime module
import datetime


def myAgeIn(unit, birthYear, birthMonth, birthDay):
    bday = datetime.datetime(birthYear, birthMonth, birthDay)
    today = datetime.datetime.now()
    if unit == "years":
        return today.year - bday.year
    elif unit == "months":
        return (today.year - bday.year) * 12 + abs(today.month - bday.month)
    elif unit == "days":
        return (today - bday).total_seconds() / 60 / 60 / 24
    elif unit == "hours":
        return (today - bday).total_seconds() / 60 / 60
    elif unit == "minutes":
        return (today - bday).total_seconds() / 60
    elif unit == "seconds":
        return (today - bday).total_seconds()
    elif unit == "milliseconds":
        return (today - bday).total_seconds() * 1000
    else:
        return "Unknown unit of time"
        