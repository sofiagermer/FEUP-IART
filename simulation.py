from collections import deque
from hill_climbing import HillClimbing
from car import Car
from intersection import Intersection
from street import Street
import file_parsing


class Simulation:
    def __init__(self, data: str):
        self.duration, self.points_per_car, self.intersections, self.streets, self.cars = file_parsing.parse(data)
        self.points = 0

    def run(self):
        pass
        #solution = HillClimbing(self.cars,self.intersections, self.streets)
        #print("yupi")
        # for _ in range(self.duration):
        #     for car in self.cars:
        #         if car.move():
        #             self.points += 1000

        #     for intersection in self.intersections:
        #         intersection.update_semaphores()

        # point_obtained = self.points
        # self.points = 0
        # print("Simulation finished: " + point_obtained + " points")
        # return point_obtained

