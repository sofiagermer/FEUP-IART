from car import Car
from intersection import Intersection
from street import Street


def parse(file_path):
    with open(file_path) as f:
        lines = f.read().splitlines()
    
    if lines == None:
        raise Exception('error: Could not read file')

    params = lines[0].split()
    duration = params[0] # in seconds
    intersection_num = params[1]
    street_num = params[2]
    car_num = params[3]
    points_per_car = params[4]  # bonus points for each car that reaches its destination in the duration specified
    streets = __parse_streets(lines)
    cars = __parse_cars(lines)


def __parse_streets(lines):


    return None

def __parse_cars(lines):
    return None