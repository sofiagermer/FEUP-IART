import unittest
import os

from car import Car
from intersection import Intersection
from solution import Solution
from street import Street
from hill_climbing import HillClimbing
from simulated_annealing import SimulatedAnnealing
from algorithm_interface import AlgorithmInterface
from simulation import Simulation
import file_parsing
from collections import deque
from algorithm_utils import gen_neighbour_lightOrOrder_func


class Program:
    """
    Class holds the main logic and menus of the program
    """
    def __init__(self):
        pass

    def run(self):
        pass


if __name__ == "__main__":
    sim_duration, points_per_car, intersections, streets, cars = file_parsing.parse("data/input/e.txt")
    simulation = Simulation(sim_duration, points_per_car, intersections, streets, cars)

    simulated_annealing = SimulatedAnnealing(simulation)
    neighbour_func = gen_neighbour_lightOrOrder_func(50, 3)

    bestSol, bestPoints = simulated_annealing.execute(neighbour_func)

    print("Best points obtained: ", bestPoints)


