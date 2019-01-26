import optuna
from .Optimizer import Optimizer
from ..Problem import Problem
class OptunaOptimizer(Optimizer):
    def __init__(self, problem:Problem):
        super().__init__(problem)
        def objective(trial):
            """Optuna Wrapper for the objective function"""
            trial.suggest_uniform()



