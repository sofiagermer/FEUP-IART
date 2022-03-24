class Intersection:
    def __init__(self, id):
        """
        :param id: unique id of the intersection
        """
        self.id = id
        self.incoming = []
        self.outgoing = []
        self.green_street_index = -1 #defined by the algorithm
        self.green_street = None #defined by the algorithm
        self.counter = 0

    def add_incoming(self, street):
        self.incoming.append(street)

    def add_outgoing(self, street):
        self.outgoing.append(street)
    
    def update_semaphores(self):
        self.counter += 1
        if self.counter == self.green_street.light_duration:
            self.green_street.green_light = False
            self.green_street_index = (self.green_street_index + 1) % len(self.incoming)
            self.green_street = self.incoming[self.green_street_index]
            self.green_street = True
            self.counter = 0


        