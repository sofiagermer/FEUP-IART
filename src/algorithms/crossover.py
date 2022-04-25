from abc import ABC, abstractmethod
from copy import copy
import random

from algorithms.solution import Solution

class Crossover(ABC):
    @abstractmethod
    def execute(self, parent1, parent2):
        pass


class OnePointCrossover(Crossover):
    def execute(self, parent1: Solution, parent2: Solution) -> Solution:
        cut_point = random.randint(1, len(parent1.state)-1)

        offspring1 = []
        offspring2 = []

        for i in range(0, cut_point):
            offspring1.append(copy(parent1.state[i]))
            offspring2.append(copy(parent2.state[i]))

        for i in range(cut_point, len(parent1.state)):
            offspring1.append(copy(parent2.state[i]))
            offspring2.append(copy(parent1.state[i]))

        return Solution(None, offspring1), Solution(None, offspring2)