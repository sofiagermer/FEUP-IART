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
        self.file_parser = FileParser(data)
        FileParser.parse_input(self)
        pass

    def add_car(self, car):
        self.cars.append(car)

    def add_street(self, street):
        self.streets.append(street)

    def add_intersection(self, intersection):
        self.intersection.append(intersection)

    def set_seconds(self, secs: int):
        self.seconds = secs

    def HillClimbing_solution(self):
        pass


