import numpy
from copy import deepcopy

class Solution:
    def __init__(self, simulation):
        st = []
        for intersection in simulation.intersections:
            intersection_streets = numpy.array([[street.name, 0] for street in intersection.incoming])
            st.append(intersection_streets)

        self.state = numpy.array(st, dtype=object)

    def export_solution(self, simulation):
        """
        Imports solution to simulation
        Simulation needs to have all light duration = 0 and green_streets = []
        """
        for street_data in self.solution:
            street = simulation[street_data[0]]
            street.light_duration = street_data[1]
            street.end_intersection.green_streets.append(street)

