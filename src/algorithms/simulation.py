import pygame

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

        return self.points
        

    def run_visualization(self,visualization, solution):
        if solution is not None:
            self.reset_state()
            self.import_solution(solution)
        car_counter = 0
        self.points = 0

        first = False

        pygame.init()
        clock = pygame.time.Clock()
        run = True

        #SOLUTION VISUALIZATION
        WIDTH, HEIGHT = 1100 , 750
        WIN = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Solution Visualization - Traffic Signaling")
        FPS = 60
        

                    
        for i in range(self.duration):
            pygame.time.wait(1000)
            # Update Each Car Position's after 1 second
            cars_that_change_street_before = []
            cars_that_change_street_after = []
            cars_that_move_foward = []

            for car in self.cars:
                old_street = car.streets[car.current_street_index]
                old_time_to_intersectioion = car.time_to_intersection
                
                #if the car has already finished its path, add 1 point
                if car.finished_path is True:
                    self.points += 1

                if car.move():
                    if first is False:
                        first = True
                    car.finished_path = True
                    self.points += self.points_per_car
                    car_counter += 1
                
                new_street = car.streets[car.current_street_index]
                new_time_to_intersectioion = car.time_to_intersection

                if(old_street != new_street):
                    if(new_street.length == car.time_to_intersection):
                        cars_that_change_street_after.append(car)

                    else:
                        print("car changed to ", car.streets[car.current_street_index].name)
                        cars_that_change_street_before.append(car)

                elif(old_time_to_intersectioion != new_time_to_intersectioion):
                    print("car moved foward in ", car.streets[car.current_street_index].name)
                    cars_that_move_foward.append(car)

            for car in cars_that_change_street_before:
                visualization.change_car_street(car)
            visualization.draw_window(self.streets,i, car_counter, self.points)

            for _ in range (100):
                for car in cars_that_move_foward:
                    visualization.update_car_position(car, car.streets[car.current_street_index])
                visualization.draw_window(self.streets,i, car_counter, self.points)

            for car in cars_that_change_street_after:
                visualization.change_car_street(car)
            visualization.draw_window(self.streets,i, car_counter, self.points)

            # Update Each Semaphore State  after 1 second
            for intersection in self.intersections:
                intersection.update_semaphores()

        for car in self.cars:
            car.finished_path = False

        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                visualization.draw_window(self.streets,self.duration, car_counter, self.points)
        pygame.quit()

        return self.points
