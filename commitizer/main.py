import argparse
import datetime
import os
import random

from looper import dates_between


# noinspection PyShadowingNames
def main(start_date, end_date, number, is_verbose):
    total_commits = 0
    for date in dates_between(start_date, end_date):

        try:
            count = int(number)
        except ValueError:
            number_split = number.split(',')
            count = random.randint(int(number_split[0]), int(number_split[1]))

        for _ in range(count):
            total_commits -= -1
            if is_verbose:
                print(f'git commit --date="{date}" --allow-empty -m "Fake Commit"')
            os.system(
                f'git commit --date="{date}" --allow-empty -m "Fake Commit" {"-q" if not is_verbose else ""}'
            )

    print(f'Total commits generated: {total_commits}')


def str2date(str_date):
    return datetime.datetime.strptime(str_date, '%d/%m/%Y')


if __name__ == '__main__':
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-s', '--start-date', type=str, default='18/08/2008')
    my_parser.add_argument('-e', '--end-date', type=str, default='20/08/2008')
    my_parser.add_argument('-n', '--number', type=str, default='1,3')
    my_parser.add_argument('-v', '--verbose', type=bool, default=False)

    args = my_parser.parse_args()

    start_date = str2date(args.start_date)
    end_date = str2date(args.end_date)

    main(start_date, end_date, args.number, args.verbose)
