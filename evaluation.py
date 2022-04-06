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

    def evaluate(self, data:str):
        file_parsing.parse_output(data, self.intersections, self.streets)

        for _ in range(self.duration):
            print('=================== 1 SEGUNDO PASSOU ========================')
            for street in self.streets:
                if self.streets[street].green_light:
                    print(self.streets[street].name , " -> verde")
                else:
                    print(self.streets[street].name , " -> vermelho")
            for car in self.cars:
                print(' ----------------- CARRO ----------------------------- ')
                #one point for each second after the car finished the path.
                if car.reached_end_path():
                    self.points += 1
                
                #moving the car foward
                else:
                    #when function move returns true -> car has just reached the end of its path
                    if(car.move(self.streets)):
                        self.points += self.points_per_car
                print(' ')
                
            for intersection in self.intersections:
                intersection.update_semaphores(self.streets)

        print("points: ", self.points)
        return self.points
