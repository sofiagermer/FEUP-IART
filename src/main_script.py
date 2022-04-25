import unittest

from car import Car
from intersection import Intersection
from solution import Solution
from street import Street
from hill_climbing import HillClimbing
from simulated_annealing import SimulatedAnnealing
from algorithm_interface import AlgorithmInterface
from simulation import Simulation
import file_parsing
from algorithm_utils import gen_neighbour_lightOrOrder_func

import matplotlib.pyplot as plt
import time

from visualization import Visualization

class Program:
    """
    Class holds the main logic and menus of the program
    """
    def __init__(self):
        pass

    def run(self):
        pass

if __name__ == "__main__":
    sim_duration, points_per_car, intersections, streets, cars = file_parsing.parse("data/input/a.txt")
    simulation = Simulation(sim_duration, points_per_car, intersections, streets, cars)

    # HILL CLIMBING SIMULATION
    hill_climbing = HillClimbing(simulation)
    neighbour_func = gen_neighbour_lightOrOrder_func(50, 3)
    hill_climbing.execute(neighbour_func)
    bestSol, bestPoints = hill_climbing.get_solution()

    visualization = Visualization(simulation.duration, simulation.points_per_car, simulation.intersections, simulation.streets, simulation.cars)

    simulation.run_visualization(visualization, bestSol)
 

