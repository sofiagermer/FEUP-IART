class Intersection:
    def __init__(self, id):
        """
        :param id: unique id of the intersection
        """
        self.id = id
        self.incoming = []
        self.outgoing = []
        self.car_in_intersection = None
        self.green_streets = []
        self.green_street_index = 0
        self.counter = 0

    def add_incoming(self, street):
        self.incoming.append(street)

    def add_outgoing(self, street):
        self.outgoing.append(street)
    
    def update_semaphores(self, streets):
        if self.car_in_intersection is not None:
            _car = self.car_in_intersection

            _car.streets[_car.current_street_index].car_list.popleft()
            _car.current_street_index += 1
            _car.streets[_car.current_street_index].car_list.append(_car)
            _car.time_to_intersection = _car.streets[_car.current_street_index].length - 1
            self.car_in_intersection = None

        #intersection doesn't has streets which can be green
        if len(self.green_streets) == 0:
            return
            
        #intersection only has got one street that is always green
        if len(self.green_streets) == 1:
            return

        #intersection has more that one semaphore which light can turn green
        self.counter += 1

        #time of currrent green semaphore has ended
        if self.counter == streets[self.green_streets[self.green_street_index]].light_duration:
            self.counter = 0 

            streets[self.green_streets[self.green_street_index]].green_light = False
            self.green_street_index += 1

            self.green_street_index = self.green_street_index % len(self.green_streets)
                
            streets[self.green_streets[self.green_street_index]].green_light = True
        
