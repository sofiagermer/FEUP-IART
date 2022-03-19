class Intersection:
    def __init__(self, id):
        """
        :param id: unique id of the intersection
        """
        self.id = id
        self.incoming = {}
        self.outgoing = {}
        self.light = None

    def add_incoming(self, street):
        self.incoming[street.name] = street

    def add_outgoing(self, street):
        self.outgoing[street.name] = street
