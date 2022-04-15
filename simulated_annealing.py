from car import Car
from intersection import Intersection
from street import Street
from algorithm_interface import AlgorithmInterface
from simulation import Simulation
from solution import Solution
import copy


class SimulatedAnnealing(AlgorithmInterface):

    def __init__(self, simulation):
        self.simulation = simulation
        self.best_solution = Solution(simulation)

    def execute(self, neighbour_func):
        self.best_solution.gen_random_solution(10)
        self.simulation.import_solution(self.best_solution)
        best_points = self.simulation.run(solution=self.best_solution)

        #loop
        new_solution = neighbour_func(self.best_solution)
        new_points = self.simulation.run(solution=new_solution)


    def get_solution(self):
        return self.best_solution
    