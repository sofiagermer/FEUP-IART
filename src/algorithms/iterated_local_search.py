from copy import deepcopy

from .algorithm_interface import AlgorithmInterface
from .solution import Solution
from .hill_climbing import HillClimbing

class IteratedLocalSearch(AlgorithmInterface):
    def __init__(self, simulation, max_iterations = 10):
        self.simulation = simulation
        self.best_solution = Solution(simulation)
        self.best_points = 0
        self.max_iterations = max_iterations


    def __mutation(self, solution, neighbour_func):
        new_solution = Solution(self.simulation, deepcopy(solution.state))
        for _ in range(5):
            new_solution = neighbour_func(new_solution)
        
        return new_solution

    def execute(self, neighbour_func, start_solution=None, start_points=None):
        iterations = 0
        hill_climbing = HillClimbing(self.simulation)
        if start_solution is None:
            hill_climbing.execute(neighbour_func)
            solution, points = hill_climbing.get_solution()
        else:
            solution = start_solution
            points = start_points

        while iterations != self.max_iterations:
            new_solution = self.__mutation(solution, neighbour_func)
            new_solution = hill_climbing.execute(neighbour_func, new_solution)
            self.simulation.reset_state()
            new_points = self.simulation.run(new_solution)
            if new_points > points:
                print("points" +  str(new_points))
                solution = new_solution
                points = new_points
            iterations += 1

        return solution, points