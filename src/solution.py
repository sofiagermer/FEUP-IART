import numpy
from random import randint

import numpy as np


class Solution:
    def __init__(self, simulation=None, state=None):
        if state is not None:
            self.state = state
        else:
            st = []
            self.simulation = simulation
            for intersection in simulation.intersections:
                intersection_streets = numpy.array([[street.name, 0] for street in intersection.incoming], dtype=object)
                st.append(intersection_streets)

            self.state = numpy.array(st, dtype=object)

    def gen_random_solution(self, max_val):
        """
        Generates a random solution
        """
        for intersection in self.state:
            for street in intersection:
                street[1] = randint(0, max_val)
            numpy.random.shuffle(intersection)

    def gen_greedy_solution(self):
        durations = {}
        for car in self.simulation.cars:
            for street in car.streets:
                if street.name in durations:
                    durations[street.name] += 1
                else:
                    durations[street.name] = 1

        for intersection in self.state:
            for street in intersection:
                if street[0] in durations:
                    street[1] = durations[street[0]]
            _gcd = np.gcd.reduce(intersection[:, 1])
            for street in intersection:
                street[1] = street[1] // _gcd
