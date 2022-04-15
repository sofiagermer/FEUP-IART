from collections import deque
from hill_climbing import HillClimbing
from car import Car
from intersection import Intersection
from street import Street
from solution import Solution
import file_parsing


class Simulation:
    def __init__(self, duration, points_per_car, intersections, streets, cars):
        self.duration = duration
        self.points_per_car = points_per_car
        self.intersections = intersections
        self.streets = streets
        self.cars = cars
        self.points = 0

    def reset_state(self):
        for intersection in self.intersections:
            intersection.reset_state()

        for street in list(self.streets.values()):
            street.reset_state()
        
        for car in self.cars:
            car.reset_state()

    def import_solution(self, solution):
        for intersection_id in range(len(solution.state)):
            intersection = self.intersections[intersection_id]
            for [name, green_duration] in solution.state[intersection_id]:
                street = self.streets[name]
                street.light_duration = green_duration

                if green_duration != 0:
                    if len(intersection.green_streets) == 0:
                        street.green_light = True
                    intersection.green_streets.append(street)


    def run(self, solution=None):
        if solution is not None:
            self.reset_state()
            self.import_solution(solution)

        car_counter = 0
        self.points = 0

        first = False


        for i in range(self.duration):

            # Update Each Car Position's after 1 second
            for car in self.cars:

                #if the car has already finished its path, add 1 point
                if car.finished_path is True:
                    self.points += 1

                if car.move():
                    if first is False:
                        print("First car: ", i)
                        first = True
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
        return Solution(self), self.points

    def evaluate_solution(self, data: str, solution):
        #file_parsing.parse_output(data, self.intersections, self.streets)
        _, points = self.run(solution)
        return points
