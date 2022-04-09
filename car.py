from pickle import TRUE


class Car:
    def __init__(self, streets):
        """
        :param streets: path that the car will take
        """
        self.streets = streets
        self.current_street_index = 0
        self.time_to_intersection = 0        

    def move_red_light(self):
        #Car is in the Middle of the Street:
        if self.time_to_intersection != 0:
            self.time_to_intersection -= 1

        #Car joins waiting line to leave Intersection
        if self.time_to_intersection == 0 and (not self.last_street()) :
            self.streets[self.current_street_index].car_list.append(self)
    
        #If Car is in Intersection -> also return False
        return False

    def move_green_light(self):

        #Car is already at the end of its path
        if self.reached_end_path():
            return True 
        
        #Car is in the Middle of the Street and Moves
        if self.time_to_intersection != 0:
            self.time_to_intersection -= 1
           
        #Car is at Intersection
        else:
            #Queue of Cars is empty
            if not self.streets[self.current_street_index].car_list:
                self.current_street_index += 1
                self.time_to_intersection = self.streets[self.current_street_index].length
                # Car moves to next street
                self.time_to_intersection -= 1
            
            #There are cars in the "waiting line"
            else :
                on_front =  self.streets[self.current_street_index].car_list[0]
                #Car is on front of queue, so it moves
                if on_front == self:
                    self.streets[self.current_street_index].car_list.popleft()
                    self.current_street_index += 1
                    self.time_to_intersection = self.streets[self.current_street_index].length
                    self.time_to_intersection -=1

                #There are other cars in front of it
                elif not self.last_street:
                    self.streets[self.current_street_index].car_list.append(self)
        
        #After moving car it may reach the end of it's path
        return self.reached_end_path()
    
    def move(self, all_streets): # Atribute all streets is needed because trafic light signalign is defined in output file
        #Light is Red
        if not all_streets[self.streets[self.current_street_index].name].green_light:
            return self.move_red_light()

        #Light is Green
        elif all_streets[self.streets[self.current_street_index].name].green_light:
            return self.move_green_light()
        
        return False

    def last_street(self):
        return self.current_street_index == (len(self.streets)-1)

    def reached_end_path(self):
        return self.last_street() and self.time_to_intersection == 0 

