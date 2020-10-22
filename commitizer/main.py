import os

from looper import dates_between


def main():
    for date in dates_between():
        print(f'git commit --date="{date}" --allow-empty -m "Fake Commit"')
        os.system(f'git commit --date="{date}" --allow-empty -m "Fake Commit"')


if __name__ == '__main__':
    main()
