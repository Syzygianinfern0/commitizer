from datetime import date
from datetime import timedelta


def dates_between(start_date=date(2008, 8, 15), end_date=date(2008, 9, 15)):
    # date(yyyy, (m)m, (d)d)
    delta = end_date - start_date  # as timedelta

    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        # print(day)
        yield day


if __name__ == '__main__':
    for date in dates_between():
        print(date)
