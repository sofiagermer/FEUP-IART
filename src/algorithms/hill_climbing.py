from .algorithm_interface import AlgorithmInterface
from .solution import Solution



class HillClimbing(AlgorithmInterface):
    
    def __init__(self, simulation):
        self.simulation = simulation
        self.best_solution = Solution(simulation)
        self.best_points = 0

    def execute(self, neighbour_func, num_iterations=1000, solution=None):
        all_points = []

        if solution is None:
            self.best_solution.gen_random_solution(10)
        else:
            self.best_solution = solution
        self.best_points = self.simulation.run(solution=self.best_solution)

        print("points" + str(self.best_points))
        no_improvement = 0

        for _ in range(num_iterations):

            if no_improvement == 50:
                break

            new_solution = neighbour_func(self.best_solution)
            new_points = self.simulation.run(solution=new_solution)

            if new_points > self.best_points:
                self.best_points = new_points
                self.best_solution = new_solution
            
            else:
                no_improvement += 0 #can be changed

            all_points.append(self.best_points)


    def get_solution(self):
        return self.best_solution, self.best_points
    