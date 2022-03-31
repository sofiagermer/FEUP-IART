import unittest
import os

from car import Car
from intersection import Intersection
from street import Street
from hill_climbing import HillClimbing
from simulated_annealing import SimulatedAnnealing
from algorithm_interface import AlgorithmInterface
from simulation import Simulation
import file_parsing


if __name__ == '__main__':
    simulation = Simulation("data/b.txt")

    hillClimbing = HillClimbing()
    simulation.execute(hillClimbing)
