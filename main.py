import unittest
import os

from Car import Car
from Intersection import Intersection
from Street import Street
from Hill_climbing import HillClimbing
from File_Parser import FileParser


class Main:

    def __init__(self, data: str):

        self.cars = []
        self.intersection = []
        self.streets = []
        self.seconds = 0
        self.pointsPerCar = 0
        self.points = 0
        self.file_parser = FileParser(data)
        FileParser.parse_input(self)

    def hillclimbing_solution(self):
        hillClimbingAlg = HillClimbing
        x = 0
        while x < self.seconds:
            pass



