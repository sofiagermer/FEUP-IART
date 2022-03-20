from car import Car
from intersection import Intersection
from street import Street


def parse(file_path):
    with open(file_path) as f:
        lines = f.read().splitlines()
    
    if lines == None:
        raise Exception('error: Could not read file')

    params = lines[0].split()
    duration = int(params[0])   # in seconds
    intersection_num = int(params[1])
    street_num = int(params[2])
    car_num = int(params[3])
    points_per_car = int(params[4])  # bonus points for each car that reaches its destination in the duration specified
    intersections = __create_intersections(intersection_num)
    streets = __parse_streets(lines[1:street_num+1], intersections)
    cars = __parse_cars(lines[street_num+1:street_num+car_num+1], streets)

    return duration, points_per_car, intersections, streets, cars


def __create_intersections(intersection_num):
    return [Intersection(i) for i in range(0, intersection_num)]

def __parse_streets(lines, intersections):
    streets = {}

    for line in lines:
        vals = line.split()

        start_intersection = int(vals[0])
        end_intersection = int(vals[1])
        name = vals[2]
        length = int(vals[3])

        street = Street(name, length, start_intersection, end_intersection)
        streets[name] = street

        intersections[street.start_intersection].add_outgoing(street)
        intersections[street.end_intersection].add_incoming(street)

    return streets

def __parse_cars(lines, streets):
    cars = []

    for line in lines:
        vals = line.split()
        cars.append(Car([streets[name] for name in vals[1:]]))

    return cars