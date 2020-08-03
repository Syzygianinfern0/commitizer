from terminal import Terminal

COMMIT_CMD = 'git commit --date="{}" --allow-empty -m "{}" '

if __name__ == '__main__':
    terminal_instance = Terminal()
    # for _ in range(5):
    #     terminal_instance.execute(COMMIT_CMD.format('10 years ago', 'fake commit'))
