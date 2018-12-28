from . import Problem
import numpy as np

class ToyProblem(Problem):
    """Toy problem with known minima and value"""
        
    @property
    def global_min(self):
        """ Global Minima """
        return self.eval(self.solution)
    

    @property
    def solution(self):
        """Global minimal point, evaluating it with result at the minimal value of the solution"""
        pass 

    def distance2min(self, x):
        """Evaluate the Euler distance (or L2 distance) between a particular solution x and the global minima 
        
        Parameters
        ----------
        x : np.ndarray
            [Solution to test]
        """
        return ((x - self.solution)**2).sum()
