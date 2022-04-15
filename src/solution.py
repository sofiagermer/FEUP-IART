import numpy
from random import randint


class Solution:
    def __init__(self, simulation=None, state=None):
        if state is not None:
            self.state = state
        else:
            st = []
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

