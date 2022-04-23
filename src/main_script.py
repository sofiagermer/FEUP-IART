from tracemalloc import start
import unittest
import os

from car import Car
from chromosome import Chromosome
from intersection import Intersection
from solution import Solution
from genetic import Genetic
from street import Street
from hill_climbing import HillClimbing
from simulated_annealing import SimulatedAnnealing
from algorithm_interface import AlgorithmInterface
from simulation import Simulation
import file_parsing
from algorithm_utils import gen_neighbour_lightOrOrder_func

import matplotlib.pyplot as plt
import time
import copy



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
    #hill_climbing = HillClimbing(simulation)
    #neighbour_func = gen_neighbour_lightOrOrder_func(50, 3)
    #hill_climbing.execute(neighbour_func)
    #bestSol, bestPoints = hill_climbing.get_solution(neighbour_func)

    # SIMULATED ANNEALING
    simulated_annealing = SimulatedAnnealing(simulation)
    rand_sol = Solution(simulation)
    rand_sol.gen_random_solution(10)
    neighbour_func = gen_neighbour_lightOrOrder_func(50, 3)

<<<<<<< HEAD
 #   start = time.time()
    #all_points = simulated_annealing.execute(neighbour_func)
    #end = time.time()
    #bestSol, bestPoints = simulated_annealing.get_solution()
   # start_population = [Chromosome(bestSol, bestPoints)]
  #  for _ in range(24):
 #       solution = neighbour_func(bestSol)
#        start_population.append(Chromosome(solution, simulation.run(solution)))

    #print("Elapsed time: ", end-start)
    #print("Best points obtained: ", bestPoints)
    #plt.plot(all_points, 'o-', markersize=3)
    #plt.ylabel('Best Points')
    #plt.show()
    genetic = Genetic(simulation, max_improveless_iterations=None, max_time=999999, population_size=50, elitism_num=10,mutation_probability=0.4, mutation_ops_percentage=0.1)
    genetic.execute()
    simulation.evaluate_solution(None, genetic.get_solution())


=======
    for cooling_type in range(4):
        random_solution = Solution(state=copy.deepcopy(rand_sol.state))
        start = time.time()
        all_points = simulated_annealing.execute(0.01, cooling_type, neighbour_func, random_solution)
        end = time.time()

        bestSol, bestPoints = simulated_annealing.get_solution()
        print("Elapsed time: ", end - start)
        print("Best points obtained: ", bestPoints)
        plt.plot(all_points, 'o-', markersize=3)
        plt.ylabel("Best Solution's Points")
        plt.show()
>>>>>>> fc9bfe2b11bbf8a3f8c7e6233c178ce1b006a6cd


