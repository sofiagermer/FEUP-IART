from car import Car
from intersection import Intersection
from street import Street
from algorithm_interface import AlgorithmInterface
from simulation import Simulation
import copy


class SimulatedAnnealing(AlgorithmInterface):

    def __init__(self, simulation):
        self.simulation = copy.deepcopy(simulation)

    def execute(self):
        pass

    def get_solution(self):
        return self.simulation
    