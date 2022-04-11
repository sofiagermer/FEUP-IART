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


    def move_red_light(self):
        #Car is in the Middle of the Street:
        if self.time_to_intersection != 0:
            self.time_to_intersection -= 1

    def move_green_light(self):

        #Car is in the Middle of the Street and Moves
        if self.time_to_intersection != 0:
            self.time_to_intersection -= 1
           
        #Car is at Intersection
        else:

            on_front = self.streets[self.current_street_index].car_list[0]
            #Car is on front of queue, so it moves
            car_inside_intersection = self.streets[self.current_street_index].end_intersection.new_car_in_intersection
            if on_front == self and car_inside_intersection is False:

                self.streets[self.current_street_index].end_intersection.car_in_intersection = self
                self.streets[self.current_street_index].end_intersection.new_car_in_intersection = True

                self.current_street_index += 1
                self.streets[self.current_street_index].car_list.append(self)
                self.time_to_intersection = self.streets[self.current_street_index].length - 1

    
    def move(self):
        # Attribute all streets is needed because traffic light signaling is defined in output
        if self.finished_path is True:
            return False


        #Light is Red
        if not self.streets[self.current_street_index].green_light:
            self.move_red_light()

        #Light is Green
        else:
            self.move_green_light()

        return self.reached_end_path()


    def last_street(self):
        return self.current_street_index == (len(self.streets)-1)

    def reached_end_path(self):
        if self.last_street() and self.time_to_intersection == 0:
            self.streets[self.current_street_index].car_list.popleft()
            return True

        return False

