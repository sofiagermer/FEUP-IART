import unittest
import os

from car import Car
from intersection import Intersection
from street import Street
from hill_climbing import HillClimbing
import file_parsing

class Main:

    def __init__(self, data: str):
        self.duration, self.points_per_car, self.intersections, self.streets, self.cars = file_parsing.parse("./data/a.txt")
        self.points = 0

    def hillclimbing_solution(self):
        hillClimbingAlg = HillClimbing
        x = 0
        while x < self.seconds:
            pass



