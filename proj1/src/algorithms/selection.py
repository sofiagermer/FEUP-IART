from abc import ABC, abstractmethod
import random
from typing import List

from .chromosome import Chromosome

class SelectionMethod(ABC):

    @abstractmethod
    def execute(self, population):
        pass


class TournamentSelection(SelectionMethod):
    def __init__(self, competitor_amount):
        self.competitor_amount = 1 if competitor_amount < 1 else competitor_amount

    def execute(self, population : List[Chromosome]):
        max_competitor_amount = len(population) // 2
        competitor_amount = min(max_competitor_amount, self.competitor_amount)
        result_list = random.sample(population, k=competitor_amount*2)
        random.shuffle(result_list)
        tournament1 = result_list[:competitor_amount]
        tournament2 = result_list[competitor_amount:]
        c1 = max(tournament1, key=lambda chromosome: chromosome.fitness)
        c2 = max(tournament2, key=lambda chromosome: chromosome.fitness)
        return (c1, c2)

class RouletteSelection(SelectionMethod):
    def execute(self, population : List[Chromosome]):
        fitness = [chromosome.fitness for chromosome in population]
        lowest_fitness = min(fitness)
        fitness = [fitness_-lowest_fitness+1 for fitness_ in fitness]
        result_list = random.sample(population=population, counts=fitness, k=2)
        return tuple(result_list)