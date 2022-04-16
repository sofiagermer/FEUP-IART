from car import Car
from intersection import Intersection
from street import Street
from algorithm_interface import AlgorithmInterface
from simulation import Simulation
from solution import Solution

import matplotlib.pyplot as plt
from math import log, exp
import random
import time

class SimulatedAnnealing(AlgorithmInterface):

    def __init__(self, simulation):
        self.simulation = simulation
        self.best_solution = Solution(simulation)
        self.best_points = 0

        self.init_temperature = 100
        self.runs_per_temp = 30 #iterations per temperature
        self.min_temperature = 0.001

    def execute(self, neighbour_func):

        all_points = []

        self.best_solution.gen_random_solution(10)
        self.simulation.import_solution(self.best_solution)
        self.best_points = self.simulation.run(solution=self.best_solution)


        counter = 0
        while counter < 1000:
            temperature = self.cooling(counter)
            if (temperature < self.min_temperature):
                print("Too cold :(, Stopped algorith")
                break
            for _ in range(self.runs_per_temp):
                counter += 1
                new_solution = neighbour_func(self.best_solution)
                new_points = self.simulation.run(solution=new_solution)

                if new_points > self.best_points:
                    self.best_points = new_points
                    self.best_solution = new_solution

                    all_points.append(new_points)

                else:
                    delta = new_points - self.best_points

                    if exp(delta/temperature) > random.random():
                        self.best_points = new_points
                        self.best_solution = new_solution

                        all_points.append(new_points)


        return all_points
        plt.plot(all_points, 'o-', markersize=3)
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
