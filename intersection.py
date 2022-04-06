class Intersection:
    def __init__(self, id):
        """
        :param id: unique id of the intersection
        """
        self.id = id
        self.incoming = []
        self.outgoing = []
        self.green_streets = []
        self.green_street_index = 0
        self.counter = 0

    def add_incoming(self, street):
        self.incoming.append(street)

    def add_outgoing(self, street):
        self.outgoing.append(street)
    
    def update_semaphores(self, streets):
        #intersection doesn't has streets which can be green
        if len(self.green_streets) == 0:
            return
            
        #intersection only has got one street that is always green
        if len(self.green_streets) == 1:
            return

        #intersection has more that one semaphore which light can turn green
        self.counter += 1
        print("self counter : ", self.counter)
        print("self.green_streets[self.green_street_index]" , self.green_streets[self.green_street_index].light_duration)

        if self.counter == self.green_streets[self.green_street_index].light_duration:
            self.counter = 0
            print("same values")
            streets[self.green_streets[self.green_street_index].name].green_light = False
            self.green_street_index += 1
            if(self.green_street_index == len(self.green_streets)):
                self.green_streets_index = 0
            #erro aqui
            print("self.green_streets[self.green_street_index].name: ", self.green_streets[self.green_street_index].name)
            streets[self.green_streets[self.green_street_index].name].green_light = True
        
            print("")
        


        