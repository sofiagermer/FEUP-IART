import unittest
import os

from car import Car
from intersection import Intersection
from street import Street
from hill_climbing import HillClimbing
import file_parsing

class Main:

    def __init__(self, data: str):

        self.cars = []
        self.intersection = []
        self.streets = []
        self.seconds = 0
        self.pointsPerCar = 0
        self.points = 0

    def hillclimbing_solution(self):
        hillClimbingAlg = HillClimbing
        x = 0
        while x < self.seconds:
            pass



