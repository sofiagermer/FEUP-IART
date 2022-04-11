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
        car_counter = 0
        first = False
        for i in range(self.duration):


            # Update Each Car Position's after 1 second
            for car in self.cars:

                if car.finished_path is True:
                    self.points += 1

                if car.move():
                    car.finished_path = True
                    self.points += self.points_per_car
                    car_counter += 1

            # Update Each Semaphore State  after 1 second
            for intersection in self.intersections:
                intersection.update_semaphores(self.streets)

        for car in self.cars:
            car.finished_path = False
        print("points: ", self.points)
        print("cars that arrived on time: ", car_counter)
        return self.points

    def evaluate_solution(self, data: str):
        file_parsing.parse_output(data, self.intersections, self.streets)
        return self.run()
