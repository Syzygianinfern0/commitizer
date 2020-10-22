import argparse
import datetime
import os

from looper import dates_between


# noinspection PyShadowingNames
def main(start_date, end_date, number):
    for date in dates_between(start_date, end_date):
        for _ in range(int(number)):
            print(f'git commit --date="{date}" --allow-empty -m "Fake Commit"')
            os.system(f'git commit --date="{date}" --allow-empty -m "Fake Commit"')


if __name__ == '__main__':
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-s', '--start-date', type=str, default='18/08/2008')
    my_parser.add_argument('-e', '--end-date', type=str, default='20/08/2008')
    my_parser.add_argument('-n', '--number', type=str, default='3')

    args = my_parser.parse_args()

    start_date = datetime.datetime.strptime(args.start_date, '%d/%m/%Y')
    end_date = datetime.datetime.strptime(args.end_date, '%d/%m/%Y')
    main(start_date, end_date, args.number)
