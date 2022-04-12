from collections import deque
from hill_climbing import HillClimbing
from car import Car
from intersection import Intersection
from street import Street
import file_parsing


class Evaluation:
    def __init__(self, data: str):
        self.duration, self.points_per_car, self.intersections, self.streets, self.cars = file_parsing.parse(data)
        self.points = 0

    def evaluate(self, data: str):
        file_parsing.parse_output(data, self.intersections, self.streets)
        car_counter = 0
        first_car = 0 
        for i in range(self.duration):
            #Update Each Car Position's after 1 second
            for car in self.cars:
                #One point for each second after the car finished the path.
                if car.reached_end_path():
                    self.points += 1
                
                #Moving the car foward
                else:
                    #when function move returns true -> car has just reached the end of its path
                    if(car.move(self.streets)):
                        self.points += self.points_per_car
                        car_counter += 1

            #Update Each Semaphore State  after 1 second
            for intersection in self.intersections:
                intersection.update_semaphores(self.streets)


        # print("cars that arrived on time: ", car_counter)
        print("points: ", self.points)
        return self.points