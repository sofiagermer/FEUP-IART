class Car:
    def __init__(self, streets):
        """
        :param streets: path that the car will take
        """
        self.streets = streets
        self.current_street_index = 0
        self.time_to_intersection = 0
        self.finish_time = 0

        self.streets[self.current_street_index].queue.append(self) #Adds the car to the end of the street

    def move(self):
        """
        Function that moves the car
        :return: True if car has reached its destination, False otherwise
        """

        # if the light is red and the car is already in the end of the street, the car doesn't move
        if not self.streets[self.current_street_index].green_light and self.time_to_intersection == 0:
            return False

        on_front = self.streets[self.current_street_index].queue[0] == self

        # if the car is on the closest to the intersection, he goes to his next street
        if on_front:
            self.streets[self.current_street_index].queue.popleft()
            if self.current_street_index == len(self.streets)-1:
                return True
            else:
                self.current_street_index += 1
                self.streets[self.current_street_index].queue.append(self)
                self.time_to_intersection = self.streets[self.current_street_index].length

        # if the car is in the middle of the street, he advances
        elif self.time_to_intersection != 0:
            self.time_to_intersection -= 1

        return False
