from git import Repo


class Terminal:
    def __init__(self, branch='gh-pages'):
        self.repo = Repo(search_parent_directories=True)
        self.tests()

        self.original_branch = self.repo.active_branch

        self.repo.git.stash()
        self.repo.git.checkout(branch)

    def tests(self):
        if self.repo.bare:
            print('Init repo?')
            self.repo.init('.')

    @staticmethod
    def execute(command: str):
        """
        Executes the Given Command in the Terminal.

        :param command: The command to be run
        :return: None

        """

        # os.system(command)

    def __del__(self):
        self.repo.git.checkout(self.original_branch)
        self.repo.git.stash('pop')
