from algorithms.hill_climbing import HillClimbing
from algorithms.simulated_annealing import SimulatedAnnealing
from algorithms.tabu import TabuSeach
from algorithms.genetic import Genetic
from algorithms.iterated_local_search import IteratedLocalSearch
from algorithms.simulation import Simulation
from algorithms.solution import Solution
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
    sim_duration, points_per_car, intersections, streets, cars = file_parsing.parse("data/input/e.txt")
    simulation = Simulation(sim_duration, points_per_car, intersections, streets, cars)

    #Greedy
    """
    sol = Solution(simulation)
    start = time.time()
    sol.gen_greedy_solution()
    end = time.time()
    print(f'Points: {simulation.run(sol)}')
    print(f'time: {end-start}')
    """

    #Iterative Local Seach
    """
    iter = IteratedLocalSearch(simulation)
    sol = Solution(simulation)
    sol.gen_greedy_solution()
    points = simulation.run(sol)

    start = time.time()
    solution, best_points = iter.execute( gen_neighbour_lightOrOrder_func(50, simulation.duration), start_solution=sol, start_points=points)
    end = time.time()
    print(f'points: {best_points}')
    print(f'time: {end - start}')
    """
    '''
    start_population = []
    for i in range(100):
        solution = gen_neighbour_lightOrOrder_func(50, simulation.duration)(sol)
        p = simulation.evaluate_solution(None, solution)
        start_population.append(Chromosome(solution, p))
    genetic_utils = Genetic(simulation, max_improveless_iterations=None, max_iterations=50, population_size=100, elitism_num=20,mutation_probability=0.4, mutation_ops_percentage=0.1)
    genetic_utils.execute(start_population)
    simulation.evaluate_solution(None, genetic_utils.get_solution())
    '''

    #HILL CLIMBING SIMULATION

    
    #hill_climbing = HillClimbing(simulation)
    #neighbour_func = gen_neighbour_lightOrOrder_func(50, 3)
    #hill_climbing.execute(neighbour_func)
    #bestSol, bestPoints = hill_climbing.get_solution()

    #visualization = Visualization(simulation.intersections, simulation.streets, simulation.cars)

    #simulation.run_visualization(visualization, bestSol)

    sol = Solution(simulation)
    sol.gen_random_solution(3)

    hill_climbing = HillClimbing(simulation)
    neighbour_func = gen_neighbour_lightOrOrder_func(50, 3)
    start = time.time()
    hill_climbing.execute(neighbour_func, num_iterations=250, solution=sol)
    end = time.time()
    bestSol, best_points = hill_climbing.get_solution()
    print(f'points: {best_points}')
    print(f'time: {end - start}')

    start = time.time()
    hill_climbing.execute(neighbour_func, num_iterations=500, solution=sol)
    end = time.time()
    bestSol, best_points = hill_climbing.get_solution()
    print(f'points: {best_points}')
    print(f'time: {end - start}')

    start = time.time()
    hill_climbing.execute(neighbour_func, num_iterations=750, solution=sol)
    end = time.time()
    bestSol, best_points = hill_climbing.get_solution()
    print(f'points: {best_points}')
    print(f'time: {end - start}')


