import os


class Terminal:
    def __init__(self, branch='gh-pages'):
        self.execute(f'git checkout {branch}')

    @staticmethod
    def execute(command: str):
        """
        Executes the Given Command in the Terminal.

        :param command: The command to be run
        :return: None

        """

        os.system(command)
