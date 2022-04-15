from random import randint
import numpy as np
from solution import Solution


def gen_neighbour_lightOrOrder_func(light_odd, max_light_variation):
    """
    Generates random neighbour solution function that returns a neighbour solution
    ------
    light_odd -> odd from 0 - 100 of changing the duration of one traffic light
    max_light_variation -> amplitude of the traffic light duration variation
    """
    def ret_func(old_solution):
        solution = Solution(state=np.copy(old_solution.state))

        intersection = randint(0, len(solution.state) - 1)

        # if the intersection only has one, it can't be shuffled
        impossible_shuffle = len(solution.state[intersection]) == 1

        r = randint(1, 100)
        if light_odd >= r or impossible_shuffle is True:
            #changes traffic light duration

            street = randint(0, len(solution.state[intersection])-1)
            increment = randint(1, max_light_variation)
            if randint(0, 1) == 0:
                solution.state[intersection][street][1] += increment

            elif solution.state[intersection][street][1] <= increment:
                solution.state[intersection][street][1] = 0

            else:
                solution.state[intersection][street][1] -= increment

        else:
            #changes traffic light order
            old_order = np.copy(solution.state[intersection])
            np.random.shuffle(solution.state[intersection])

            while np.array_equal(old_order, solution.state[intersection]) is True:
                np.random.shuffle(solution.state[intersection])

        return solution

    return ret_func
