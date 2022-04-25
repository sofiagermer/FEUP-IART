import numpy
from car import Car
from intersection import Intersection
from street import Street
from algorithm_interface import AlgorithmInterface
from simulation import Simulation
from solution import Solution

import matplotlib.pyplot as plt
import math
import random

class HillClimbing(AlgorithmInterface):
    
    def __init__(self, simulation):
        self.simulation = simulation
        self.best_solution = Solution(simulation)
        self.best_points = 0

    def execute(self, neighbour_func):
        all_points = []

        self.best_solution.gen_random_solution(10)
        self.simulation.import_solution(self.best_solution)
        self.best_points = self.simulation.run(solution=self.best_solution)

        no_improvement = 0

        for _ in range(1000):

            if no_improvement == 50:
                break

            new_solution = neighbour_func(self.best_solution)
            new_points = self.simulation.run(solution=new_solution)

            if new_points > self.best_points:
                self.best_points = new_points
                self.best_solution = new_solution
            
            else:
                no_improvement += 1

            all_points.append(self.best_points)

        # plt.plot(all_points, 'o-')
        # plt.ylabel('Best Points')
        # plt.show()

    def get_solution(self):
        return self.best_solution, self.best_points
    