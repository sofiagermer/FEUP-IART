import numpy
from random import randint

import numpy as np
import copy


class Solution:
    def __init__(self, simulation=None, state=None):
        """
        Initiate the solution
        ---------------
        simulation : simulation where the solution it can be drawn from
        state : solution that can be copied
        """
        self.active_streets = {}
        if state is not None:
            self.state = state
        elif simulation is not None:
            st = []
            for intersection in simulation.intersections:
                intersection_streets = numpy.array([[street.name, 0] for street in intersection.incoming], dtype=object)
                st.append(intersection_streets)

            self.state = numpy.array(st, dtype=object)

            for car in simulation.cars:
                for street in car.streets:
                    if street.name in self.active_streets:
                        self.active_streets[street.name] += 1
                    else:
                        self.active_streets[street.name] = 1
        else:
            raise Exception("Missing simulation or state parameter")

    def gen_random_solution(self, max_val):
        """
        Generates a random solution
        -------
        max_val : maximum light_duration a street
        """
        for intersection in self.state:
            for street in intersection:
                if street[0] in self.active_streets:
                    street[1] = randint(0, max_val)
                else:
                    street[1] = 0
            numpy.random.shuffle(intersection)

    def gen_greedy_solution(self):
        """
        Generates a greedy solution
        """
        for intersection in self.state:
            for street in intersection:
                if street[0] in self.active_streets:
                    street[1] = self.active_streets[street[0]]
            _gcd = np.gcd.reduce(intersection[:, 1])
            if _gcd == 0:
                _gcd = 1
            for street in intersection:
                street[1] = street[1] // _gcd


    def copy(self):
        """
        Makes a deepcopy of a solution
        """
        new_solution = Solution(state=copy.deepcopy(self.state))
        new_solution.active_streets = self.active_streets
        return new_solution

