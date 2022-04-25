class Simulation:
    def __init__(self, duration, points_per_car, intersections, streets, cars):
        """
        Initializes the Simulation with it's elements
        --------
        duration : simulation's duration
        points_per_car : points atributed to the simulation when a car finishes its path
        instersection : list with all the intersections
        streets : dictionary with all the streets, using the streets' name as keys
        cars : list with all the cars
        """

        self.duration = duration
        self.points_per_car = points_per_car
        self.intersections = intersections
        self.streets = streets
        self.cars = cars
        self.points = 0

    def reset_state(self):
        """
        Resets the simulation to its original state
        """
        for intersection in self.intersections:
            intersection.reset_state()

        for street in list(self.streets.values()):
            street.reset_state()
        
        for car in self.cars:
            car.reset_state()

    def import_solution(self, solution):
        """
        Imports a solution to the simulation
        -------
        solution : solution to be imported
        """
        for intersection_id in range(len(solution.state)):
            intersection = self.intersections[intersection_id]
            for [name, green_duration] in solution.state[intersection_id]:
                street = self.streets[name]
                street.light_duration = green_duration

                if green_duration != 0:
                    if len(intersection.green_streets) == 0:
                        street.green_light = True
                    intersection.green_streets.append(street)


    def run(self, solution=None):
        """
        Runs the simulation
        -------
        solution : solution that can be imported before the simulation executes´

        returns the points made by the simulation

        """
        if solution is not None:
            self.reset_state()
            self.import_solution(solution)

        car_counter = 0
        self.points = 0

        first = False


        for i in range(self.duration+1):

            # Update Each Car Position's after 1 second
            for car in self.cars:

                #if the car has already finished its path, add 1 point
                if car.finished_path is True:
                    self.points += 1

                if car.move():
                    if first is False:
                        #print("First car: ", i)
                        first = True
                    car.finished_path = True
                    self.points += self.points_per_car
                    car_counter += 1


            # Update Each Semaphore State  after 1 second
            for intersection in self.intersections:
                intersection.update_semaphores()

        for car in self.cars:
            car.finished_path = False
        print("points: ", self.points)
        print("cars that arrived on time: ", car_counter)
        return self.points
