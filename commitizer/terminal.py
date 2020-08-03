import os


class Terminal:
    def __init__(self):
        pass

    @staticmethod
    def execute(command: str):
        """
        Executes the Given Command in the Terminal.

        :param command: The command to be run
        :return: None

        """

        os.system(command)
