from collections import deque


class Street:
    def __init__(self, name, length, start_intersection, end_intersection):
        """
        :param name: name of the street
        :param length: length of the street
        :param start_intersection: id of the start_intersection
        :param end_intersection: id of the end_intersection
        """
        self.name = name
        self.length = length
        self.start_intersection = start_intersection
        self.end_intersection = end_intersection
        self.queue = deque([])
