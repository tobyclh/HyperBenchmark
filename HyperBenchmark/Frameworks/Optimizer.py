from ..Problem import Problem
from scipy.optimize import optimize, minimize
import numpy as np

class Optimizer:
    def __init__(self, func:Problem):
        self.problem = func

    def minimize(self, init=None):
        pass
