from random import randint
from solution import Solution
import copy


def gen_neighbour_lightOrOrder_func(light_odd, max_light_variation):
    """
    Generates random neighbour solution function that returns a neighbour solution
    ------
    light_odd -> odd from 0 - 100 of changing the duration of one traffic light
    max_light_variation -> amplitude of the traffic light duration variation
    """
    def ret_func(old_solution):
        solution = Solution(state=copy.deepcopy(old_solution.state))

        intersection = randint(0, len(solution.state) - 1)

        # if the intersection only has one, it can't be shuffled
        impossible_shuffle = len(solution.state[intersection]) == 1

        r = randint(1, 100)
        if light_odd >= r or impossible_shuffle is True:
            #changes traffic light duration

            #print("Lights: ", intersection)
            return change_semaphore_duration(solution, intersection, max_light_variation)

        else:
            #changes traffic light order

            #print("Order: ", intersection)
            return switch_semaphore_order(solution, intersection)

    return ret_func


def change_semaphore_duration(solution, intersection, max_light_variation):
    street = randint(0, len(solution.state[intersection]) - 1)
    increment = randint(1, max_light_variation)

    print("Lights: ", intersection, street, increment)

    if randint(0, 1) == 0:
        solution.state[intersection][street][1] += increment

    elif solution.state[intersection][street][1] <= increment:
        solution.state[intersection][street][1] = 0

    else:
        solution.state[intersection][street][1] -= increment

    return solution

def switch_semaphore_order(solution, intersection):
    s1 = randint(0, len(solution.state[intersection]) - 1)
    s2 = randint(0, len(solution.state[intersection]) - 1)
    while s1 != s2:
        s2 = randint(0, len(solution.state[intersection]) - 1)

    print("Order: ", intersection, s1, s2)

    solution.state[intersection][s1], solution.state[intersection][s2] = solution.state[intersection][s2], \
                                                                         solution.state[intersection][s1]
    return solution

