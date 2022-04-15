from car import Car
from intersection import Intersection
from street import Street
from algorithm_interface import AlgorithmInterface
import copy

class HillClimbing(AlgorithmInterface):
    def __init__(self, simulation):
        self.simulation = copy.deepcopy(simulation)

    def execute(self, neighbour_func):
        pass

    def get_solution(self):
        return self.simulation
    