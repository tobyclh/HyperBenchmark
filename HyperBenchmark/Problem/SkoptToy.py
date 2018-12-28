from . import ToyProblem
from skopt.benchmarks import hart6
import numpy as np

class Hart6(ToyProblem):
    """Skopt implementation of Hart6
    Original Implementation : <https://github.com/scikit-optimize/scikit-optimize/blob/master/skopt/benchmarks.py>
    More details: <http://www.sfu.ca/~ssurjano/hart6.html>
    """

    def eval(self, x):
        return hart6(x)

    @property
    def search_space(self):
        return np.array([[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]])

    @property
    def dimension(self):
        return 6

    @property
    def solutions(self):
        return np.asarray([0.20169, 0.15001, 0.476874, 0.275332, 0.311652, 0.6573])