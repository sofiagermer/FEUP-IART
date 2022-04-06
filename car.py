from pickle import TRUE


class Car:
    def __init__(self, streets):
        """
        :param streets: path that the car will take
        """
        self.streets = streets
        self.current_street_index = 0
        self.time_to_intersection = 0

        self.streets[self.current_street_index].queue.append(self) #Adds the car to the end of the street

    def move(self, all_streets):
        """
        Function that moves the car
        :return: True if car has reached its destination, False otherwise
        """
        print(' ')

        #Street were car is currentely on has Red Light
        if(not all_streets[self.streets[self.current_street_index].name].green_light):
            print(all_streets[self.streets[self.current_street_index].name].name, " -> vermelho")
            return False

        #Current street where car is, is green, so car can move
        if(all_streets[self.streets[self.current_street_index].name].green_light):

            #Car is at the end of the street
            if self.time_to_intersection == 0:

                #Car is at the end of its path
                if(self.reached_end_path()):
                    print("Car is at the end of its path")
                    return True 
                else:
                    #Car reaches end of street
                    print("Car is in the end of the street")
                    print("old street name: ", self.streets[self.current_street_index].name)
                    self.current_street_index += 1
                    print("new street name: ", self.streets[self.current_street_index].name)
                    self.time_to_intersection = self.streets[self.current_street_index].length

                    #If next street of the car path is also green
                    if all_streets[self.streets[self.current_street_index].name].green_light: 
                        print('car is in the middle of the street and moving')
                        self.time_to_intersection -= 1

            #Car moves and gets closer to next intesection
            else: 
                print('car is in the middle of the street and moving')
                self.time_to_intersection -= 1

        return False

    def reached_end_path(self):
        if(self.current_street_index == (len(self.streets)-1)):
            print("car reached end")
            return True
        return False

