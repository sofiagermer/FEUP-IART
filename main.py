import unittest
import os

from car import Car
from intersection import Intersection
from street import Street
from hill_climbing import HillClimbing
import file_parsing


class Simulation:

    def __init__(self, data: str):
        self.duration, self.points_per_car, self.intersections, self.streets, self.cars = file_parsing.parse(data)
        self.points = 0

    def hillclimbing_solution(self):
        hillClimbingAlg = HillClimbing
        x = 0
        while x < self.seconds:
            pass

    def _run(self):
        for _ in range(self.duration):
            for x in self.cars:
                car.move()

    def execute(self, algorithm: str):
        if algorithm == "hill_climbing":
            hillclimbing_solution(self)
        _run()


if __name__ == '__main__':
    simulation = Simulation("data/b.txt")
    simulation.execute("hill_climbing")
