from pickle import TRUE


class Car:
    def __init__(self, streets):
        """
        :param streets: path that the car will take
        """
        self.streets = streets
        self.current_street_index = 0
        self.time_to_intersection = 0
        self.finished_path = False

    def reset_state(self):
        self.current_street_index = 0
        self.time_to_intersection = 0
        self.finished_path = False

    def move_green_light(self):
        if self.time_to_intersection == 0:
            on_front = self.streets[self.current_street_index].car_list[0]
            car_inside_intersection = self.streets[self.current_street_index].end_intersection.new_car_in_intersection

            #if the car is on the front of the queue AND a car hasn't traversed the intersection yet
            # (only 1 car can traversed a intersection in each second)
            if on_front == self and car_inside_intersection is False:

                self.streets[self.current_street_index].end_intersection.new_car_in_intersection = True
                self.streets[self.current_street_index].car_list.popleft()
                self.current_street_index += 1
                self.streets[self.current_street_index].car_list.append(self)
                self.time_to_intersection = self.streets[self.current_street_index].length

    
    def move(self):

        if self.finished_path is True:
            return False


        #regardless of the light, if a car is in the middle of a street, it moves
        if self.time_to_intersection != 0:
            self.time_to_intersection -= 1
            if self.reached_end_path():
                return True

            #if the light is green, it transitions to the next street
            if self.streets[self.current_street_index].green_light:
                self.move_green_light()

        else:
            #if the light is green, it transitions to the next street
            if self.streets[self.current_street_index].green_light:
                self.move_green_light()

                #if the car transitions to the next street, he can still move since traversing a intersection is instantaneous
                if self.time_to_intersection != 0:
                    self.time_to_intersection -= 1

        #checks if the car has ended its path
        return self.reached_end_path()


    def last_street(self):
        return self.current_street_index == (len(self.streets)-1)

    def reached_end_path(self):
        if self.last_street() and self.time_to_intersection == 0:
            self.streets[self.current_street_index].car_list.popleft()
            return True

        return False

