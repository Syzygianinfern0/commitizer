from datetime import date
from datetime import timedelta


def dateiter(sdate=date(2008, 8, 15), edate=date(2008, 9, 15)):
    delta = edate - sdate  # as timedelta

    for i in range(delta.days + 1):
        day = sdate + timedelta(days=i)
        print(day)


if __name__ == '__main__':
    dateiter()
