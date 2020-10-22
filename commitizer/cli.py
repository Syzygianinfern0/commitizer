import argparse

import commitizer


def main():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-s', '--start-date', type=str, default='18/08/2008')
    my_parser.add_argument('-e', '--end-date', type=str, default='20/08/2008')
    my_parser.add_argument('-n', '--number', type=str, default='1,3')
    my_parser.add_argument('-v', '--verbose', action='count', default=0)

    args = my_parser.parse_args()

    start_date = commitizer.str2date(args.start_date)
    end_date = commitizer.str2date(args.end_date)

    commitizer.main(start_date, end_date, args.number, args.verbose)
