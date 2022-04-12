import numpy
import simulation

class Solution:
    def __init__(self, simulation):
        self.solution = []
        for intersection in simulation.intersections:
            intersection_streets = []
            for street in intersection.incoming:
                intersection_streets.append([street.name, street.light_duration])

            self.solution.append(intersection_streets)

        self.solution = numpy.array(self.solution, dtype=object)

    def export_solution(self, simulation):
        """
        Imports solution to simulation
        Simulation needs to have all light duration = 0 and green_streets = []
        """
        for street_data in self.solution:
            street = simulation[street_data[0]]
            street.light_duration = street_data[1]
            street.end_intersection.green_streets.append(street)

