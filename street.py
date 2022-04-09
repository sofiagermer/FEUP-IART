from collections import deque


class Street:
    def __init__(self, name, length, start_intersection, end_intersection):
        """
        Street data class
        -------------
        :param name: name of the street (unique)
        :param length: length of the street
        :param start_intersection: id of the start_intersection
        :param end_intersection: id of the end_intersection
        """
        self.name = name
        self.length = length
        self.start_intersection = start_intersection
        self.end_intersection = end_intersection
        self.car_list = deque([])
        self.light_duration = 0 #determined by the optimization algorithm
        self.green_light = False
