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
from algorithm_utils import gen_neighbour_lightOrOrder_func

import matplotlib.pyplot as plt
import time



class Program:
    """
    Class holds the main logic and menus of the program
    """
    def __init__(self):
        pass

    def run(self):
        pass

    def mainmenu(self):
        print("=======Traffic light optimization=======")
        print("")



if __name__ == "__main__":
    sim_duration, points_per_car, intersections, streets, cars = file_parsing.parse("data/input/e.txt")
    #file_parsing.parse_output("data/output/e.txt", intersections, streets)

    simulation = Simulation(sim_duration, points_per_car, intersections, streets, cars)

    # HILL CLIMBING SIMULATION
    hill_climbing = HillClimbing(simulation)
    neighbour_func = gen_neighbour_lightOrOrder_func(50, 3)
    hill_climbing.execute(neighbour_func)
    bestSol, bestPoints = hill_climbing.get_solution(neighbour_func)

    # SIMULATED ANNEALING
    simulated_annealing = SimulatedAnnealing(simulation)
    neighbour_func = gen_neighbour_lightOrOrder_func(50, 3)
    start = time.time()
    all_points = simulated_annealing.execute(neighbour_func)
    end = time.time()
    bestSol, bestPoints = simulated_annealing.get_solution()

    print("Elapsed time: ", end-start)
    print("Best points obtained: ", bestPoints)
    plt.plot(all_points, 'o-', markersize=3)
    plt.ylabel('Best Points')
    plt.show()






