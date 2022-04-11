import unittest
import os

from car import Car
from intersection import Intersection
from street import Street
from hill_climbing import HillClimbing
from simulated_annealing import SimulatedAnnealing
from algorithm_interface import AlgorithmInterface
from simulation import Simulation
from evaluation import Evaluation
import file_parsing
from collections import deque


class Program:
    """
    Class holds the main logic and menus of the program
    """
    def __init__(self):
        pass

    def run(self):
        pass

if __name__ == "__main__":
    simulation = Simulation("data/input/a.txt")
    simulation.evaluate_solution("data/output/a.txt")

