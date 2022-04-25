from .solution import Solution
from random import randint, randrange
import numpy as np

def gen_neighbour_lightOrOrder_func(light_odd, max_light_variation):
    """
    Generates random neighbour solution function that returns a neighbour solution
    ------
    light_odd -> odd from 0 - 100 of changing the duration of one traffic light
    max_light_variation -> amplitude of the traffic light duration variation
    """
    def ret_func(old_solution):
        solution = old_solution.copy()

        intersection = randint(0, len(solution.state) - 1)

        counter = 0 #If in 100 attempts it doesn
        while counter < 100:
            while len(solution.state[intersection]) == 1: #Intersection with only one street don't need to be changed
                intersection = randint(0, len(solution.state) - 1)

            if len(set(solution.state[intersection][:,0]).intersection(solution.active_streets)) > 1:
                break

            counter+=1


        r = randint(1, 100)
        if light_odd >= r:
            #changes traffic light duration


            return change_semaphore_duration(solution, intersection, max_light_variation)

        else:
            #changes traffic light order

            return switch_semaphore_order(solution, intersection)

    return ret_func


def switch_traffic_lights(solution, _):
    intersection = randrange(0, len(solution.state))

    return switch_semaphore_order(solution, intersection)

def change_green_light_duration(solution, max_light_offset):
    intersection = randrange(0, len(solution.state))
    print("change  green light duration")
    return change_semaphore_duration(solution, intersection, max_light_offset)

def change_semaphore_duration(solution, intersection, max_light_variation):
    """
    Operators that changes a semaphore duration
    ------
    solution : solution to be changed
    intersection : solution's intersection id to be changed
    max_light_variation : amplitude of the light variation. Light will vary randomly between the values
                          [-max_light_variation , max_light_variation]


    returns the changed solution
    """
    street = randint(0, len(solution.state[intersection]) - 1)
    increment = randint(1, max_light_variation)

    # print("Lights: ", intersection, street, increment)

    if randint(0, 1) == 0:
        solution.state[intersection][street][1] += increment

    elif solution.state[intersection][street][1] <= increment:
        solution.state[intersection][street][1] = 0

    else:
        solution.state[intersection][street][1] -= increment

    return solution

def switch_semaphore_order(solution, intersection):
    """
    Operators that changes the order of the semaphores in an intersection
    ------
    solution : solution to be changed
    intersection : solution's intersection id to be changed
    returns the changed solution
    """
    s1 = randint(0, len(solution.state[intersection]) - 1)
    s2 = randint(0, len(solution.state[intersection]) - 1)
    while s1 == s2:
        s2 = randint(0, len(solution.state[intersection]) - 1)

    # print("Order: ", intersection, s1, s2)

    solution.state[intersection][s1], solution.state[intersection][s2] = solution.state[intersection][s2], \
                                                                         solution.state[intersection][s1]
    return solution

