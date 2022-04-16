from car import Car
from intersection import Intersection
from street import Street
from algorithm_interface import AlgorithmInterface
from simulation import Simulation
from solution import Solution

import matplotlib.pyplot as plt
import math
import random
import time

class SimulatedAnnealing(AlgorithmInterface):

    def __init__(self, simulation):
        self.simulation = simulation
        self.best_solution = Solution(simulation)
        self.best_points = 0

        self.init_temperature = simulation.points_per_car * 5 #seria 3000 ou 300 na maioria dos casos
        self.cooling = 0.7 #cooling coefficient
        self.runs_per_temp = 30 #iterations per temperature

    def execute(self, neighbour_func):

        all_points = []

        self.best_solution.gen_random_solution(10)
        self.simulation.import_solution(self.best_solution)
        self.best_points = self.simulation.run(solution=self.best_solution)

        self.temperature = self.init_temperature

        while(self.temperature > self.init_temperature/1000):
            for _ in range(self.runs_per_temp):
                new_solution = neighbour_func(self.best_solution)
                new_points = self.simulation.run(solution=new_solution)
                if new_points > self.best_points:
                    self.best_points = new_points
                    self.best_solution = new_solution

                    all_points.append(new_points)

                else:
                    delta = self.best_points - new_points
                    p = math.exp(-delta/self.temperature)
                    if p > random.random():
                        self.best_points = new_points
                        self.best_solution = new_solution

                        all_points.append(new_points)

            self.temperature *= self.cooling


        plt.plot(all_points, 'o-')
        plt.ylabel('Best Points')
        plt.show()

    def cooling(self, t):
        return self.quadratic_cooling(t)

    def exponential_cooling(self, t):
        return self.init_temperature * 0.7 ** t

    def log_cooling(self, t):
        return self.init_temperature / (1 + log(1 + t))

    def linear_cooling(self, t):
        return self.init_temperature / (1 + t)

    def quadratic_cooling(self, t):
        return self.init_temperature / (1 + t ** 2)

    def get_solution(self):
        return self.best_solution, self.best_points
    