from car import Car
from intersection import Intersection
from street import Street

#PARSE INPUT
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

        start_intersection = intersections[int(vals[0])]
        end_intersection = intersections[int(vals[1])]
        name = vals[2]
        length = int(vals[3])

        street = Street(name, length, start_intersection, end_intersection)
        streets[name] = street

        intersections[street.start_intersection.id].add_outgoing(street)
        intersections[street.end_intersection.id].add_incoming(street)

    return streets

def __parse_cars(lines, streets):
    cars = []

    for line in lines:
        vals = line.split()
        car = Car([streets[name] for name in vals[1:]])
        car.time_to_intersection = 0 #each car starts at the end of its initial street
        cars.append(car)

    #Add Cars to their first street queue
    for car in cars:
        car.streets[0].car_list.append(car)

    return cars


#PARSE OUPUT
def parse_output(file_path, intersections, streets):
    with open(file_path) as f:
        lines = f.read().splitlines()
    
    if lines == None:
        raise Exception('error: Could not read file')

    num_intersections = int(lines[0])
    
    current_line = 1
    for _ in range(0,num_intersections):
        curr_intersection = int(lines[current_line])
        current_line += 1
        num_streets = int(lines[current_line])
        current_line += 1
        for i in range(0, num_streets):
            params = lines[current_line].split()
            current_line += 1
            street = params[0]
            time_semaphore = int(params[1])
            streets[street].light_duration = time_semaphore
            intersections[curr_intersection].green_streets.append(street)

            if(i == 0) : 
                streets[street].green_light = True
    return
