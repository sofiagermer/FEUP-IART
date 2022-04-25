from .algorithm_interface import AlgorithmInterface
from .solution import Solution

from math import log, exp
import random


class SimulatedAnnealing(AlgorithmInterface):
    EXP_COOLING = 0
    LOG_COOLING = 1
    LIN_COOLING = 2
    QUAD_COOLING = 3

    def __init__(self, simulation):
        self.simulation = simulation
        self.best_solution = Solution(simulation)
        self.best_points = 0

        self.init_temperature = 3000
        self.runs_per_temp = 1 #iterations per temperature
        self.min_temperature = None

    def execute(self, min_temperature, cooling_type, neighbour_func, random_sol=None):
        self.min_temperature = min_temperature
        self.cooling_setup(cooling_type)

        all_points = []
        if random_sol == None:
            self.best_solution.gen_random_solution(10)
        else:
            self.best_solution = random_sol
        self.simulation.import_solution(self.best_solution)
        self.best_points = self.simulation.run(solution=self.best_solution)
        all_points.append(self.best_points)

        counter = 0
        while counter < 500:
            temperature = self.cooling(counter/self.runs_per_temp)

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


    def cooling_setup(self, cooling_type):
        if cooling_type == self.EXP_COOLING:
            self.cooling = self.exponential_cooling
        elif cooling_type == self.LOG_COOLING:
            self.cooling = self.log_cooling
        elif cooling_type == self.LIN_COOLING:
            self.cooling = self.linear_cooling
        elif cooling_type == self.QUAD_COOLING:
            self.cooling = self.quadratic_cooling
        else:
            raise Exception("Error: cooling type unavailable ")

    def exponential_cooling(self, t):
        return self.init_temperature * 0.9 ** t

    def log_cooling(self, t):
        return self.init_temperature / (1 + log(1 + 10*t))

    def linear_cooling(self, t):
        return self.init_temperature / (1 + t)

    def quadratic_cooling(self, t):
        return self.init_temperature / (1 + t ** 2)

    def get_solution(self):
        return self.best_solution, self.best_points
