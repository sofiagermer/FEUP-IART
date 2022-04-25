from .algorithm_interface import AlgorithmInterface
from .solution import Solution

from collections import deque
import random

class TabuSeach(AlgorithmInterface):
    def __init__(self, simulation):
        self.simulation = simulation
        self.best_solution = Solution(simulation)
        self.best_points = 0


    def execute(self, max_tabusize, neighbour_func, random_sol=None):
        all_points = []
        self.max_tabusize = max_tabusize
        self.tabu_list = deque([])

        if random_sol == None:
            self.best_solution.gen_random_solution(10)
        else:
            self.best_solution = random_sol
        self.simulation.import_solution(self.best_solution)
        self.best_points = self.simulation.run(solution=self.best_solution)
        all_points.append(self.best_points)

        best_candidate = self.best_solution
        self.update_tabulist(best_candidate)
        counter = 0
        while counter < 50:
            nbh = []
            for x in range(10):
                nbh.append(neighbour_func(best_candidate))

            best_candidate, best_candidate_points = self.best_admissable_sol(nbh)

            if best_candidate_points > self.best_points:
                self.best_solution = best_candidate
                self.best_points = best_candidate_points
                all_points.append(best_candidate_points)

            self.update_tabulist(best_candidate)

            counter += 1

        return all_points


    def best_admissable_sol(self, nbh):
        best_sol = None
        best_points = 0
        for sol in nbh:
            new_points = self.simulation.run(sol)
            if new_points > best_points:
                if not(self.in_tabulist(sol)) and (new_points > best_points): #errado, não se pode checkar se sol está na tabu_list desta forma
                    best_sol = sol
                    best_points = new_points

                #aspiration criteria
                elif self.aspiration(sol, new_points):
                    best_sol = sol
                    best_points = new_points

        return best_sol, best_points

    def in_tabulist(self, solution):
        for tabu_sol in self.tabu_list:
            if solution.state == tabu_sol.state:
                return True

        return False

    def update_tabulist(self, solution):
        self.tabu_list.append(solution)
        if len(self.tabu_list) > self.max_tabusize:
            self.tabu_list.popleft()

    def aspiration(self, sol, new_points):
        return self.no_aspiration()

    def no_aspiration(self):
        return False

    def get_solution(self):
        return self.best_solution, self.best_points
