import unittest
import os

from car import Car
from intersection import Intersection
from street import Street
from hill_climbing import HillClimbing
from simulated_annealing import SimulatedAnnealing
from algorithm_interface import AlgorithmInterface
import file_parsing


class Simulation:

    def __init__(self, data: str):
        self.duration, self.points_per_car, self.intersections, self.streets, self.cars = file_parsing.parse(data)
        self.points = 0

    def run(self):
        for _ in range(self.duration):
            for car in self.cars:
                if car.move():
                    self.points += 1000

            for intersection in self.intersections:
                intersection.update_semaphores()

    def execute(self, algorithm):
        algorithm.execute(self)
        self.run()
        print("Simulation finished: " + self.points + " points")
        self.points = 0


if __name__ == '__main__':
    simulation = Simulation("data/b.txt")

    hillClimbing = HillClimbing()
    simulation.execute(hillClimbing)
