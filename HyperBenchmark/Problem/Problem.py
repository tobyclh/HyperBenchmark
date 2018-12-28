class Problem:
    """Base class of problem for benchmarking"""

    def __init__(self):
        return

    @property
    def search_space(self):
        pass

    @property
    def dimension(self):
        return None

    def eval(self, x):
        pass
    