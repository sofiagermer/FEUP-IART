from algorithms.solution import Solution
from algorithms.hill_climbing import HillClimbing
from algorithms.simulated_annealing import SimulatedAnnealing
from algorithms.tabu import TabuSeach
from algorithms.simulation import Simulation
import file_parsing
from algorithms.algorithm_utils import gen_neighbour_lightOrOrder_func

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


    def mainmenu(self):
        print("=======Traffic light optimization=======")
        print("")


if __name__ == "__main__":
    sim_duration, points_per_car, intersections, streets, cars = file_parsing.parse("data/input/b.txt")
    simulation = Simulation(sim_duration, points_per_car, intersections, streets, cars)

    sol = Solution(simulation)
    start = time.time()
    sol.gen_greedy_solution()
    end = time.time()
    print(f'Points: {simulation.run(sol)}')

    print(f'time: {end-start}')

    # HILL CLIMBING SIMULATION
    """
    
    hill_climbing = HillClimbing(simulation)
    neighbour_func = gen_neighbour_lightOrOrder_func(50, 3)
    hill_climbing.execute(neighbour_func)
    bestSol, bestPoints = hill_climbing.get_solution()

    visualization = Visualization(simulation.intersections, simulation.streets, simulation.cars)

    simulation.run_visualization(visualization, bestSol)

    #hill_climbing = HillClimbing(simulation)
    #neighbour_func = gen_neighbour_lightOrOrder_func(50, 3)
    #hill_climbing.execute(neighbour_func)
    #bestSol, bestPoints = hill_climbing.get_solution(neighbour_func)
    """
    # SIMULATED ANNEALING
    """
    simulated_annealing = SimulatedAnnealing(simulation)
    sol = Solution(simulation)
    sol.gen_greedy_solution()
    #sol.gen_random_solution(10)
    neighbour_func = gen_neighbour_lightOrOrder_func(50, 3)

    for cooling_type in range(4):
        random_solution = sol.copy()
        start = time.time()
        all_points = simulated_annealing.execute(0.001, cooling_type, neighbour_func, random_solution)
        end = time.time()

        bestSol, bestPoints = simulated_annealing.get_solution()
        print("Elapsed time: ", end - start)
        print("Best points obtained: ", bestPoints)
        plt.plot(all_points, 'o-', markersize=3)
        plt.ylabel("Best Solution's Points")
        plt.show()
    """

    # Tabu Search
    """
    tabu_search = TabuSeach(simulation)
    sol = Solution(simulation)
    sol.gen_greedy_solution()
    neighbour_func = gen_neighbour_lightOrOrder_func(50, 3)
    start = time.time()
    best_cand_points = tabu_search.execute(20, neighbour_func, sol)
    end = time.time()

    bestSol, bestPoints = tabu_search.get_solution()
    print("Elapsed time: ", end - start)
    print("Best points obtained: ", bestPoints)
    plt.plot(best_cand_points, 'o-', markersize=3)
    plt.ylabel("Points")
    plt.show()
    """


