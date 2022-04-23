import math
import random
from typing import List

from algorithm_interface import AlgorithmInterface
from algorithm_utils import change_green_light_duration, switch_traffic_lights
from chromosome import Chromosome
from crossover import OnePointCrossover
from selection import RouletteSelection
from solution import Solution
from timeit import default_timer as timer

class Genetic(AlgorithmInterface):
    def __init__(self, simulation, max_iterations=None, max_improveless_iterations=15, max_time=None, selection_method=None,
                crossover=None, population_size=25, mutation_probability=0.2, mutation_ops_percentage=0.01, 
                elitism=True, elitism_num = 5):
        self.simulation = simulation
        self.max_iterations = max_iterations
        self.max_improveless_iterations = max_improveless_iterations
        self.max_time = max_time
        self.selection_method = RouletteSelection() if selection_method is None else selection_method
        self.crossover = OnePointCrossover() if crossover is None else crossover
        self.population_size = population_size
        self.mutation_probability = mutation_probability
        self.mutations = [switch_traffic_lights, change_green_light_duration]
        self.mutation_ops_percentage = mutation_ops_percentage
        self.elitism = elitism
        self.elitism_num = elitism_num

    def stop(self):
        return self.max_iterations is not None and self.iterations == self.max_iterations or \
               self.max_improveless_iterations is not None and self.improveless_iterations == self.max_improveless_iterations or \
               self.max_time is not None and timer() - self.start_time >= self.max_time

    def execute(self, start_population=None):
        self.iterations = 0
        self.improveless_iterations = 0
        self.start_time = timer()
        population = self.__random_population() if start_population == None else start_population
        self.best_solution = Chromosome(None, -999999)

        while True:
            if self.stop(): break

            population = self.__new_generation(population)
            new_best_solution = self.__get_best_solution(population)

            if new_best_solution.fitness > self.best_solution.fitness:
                self.improveless_iterations = 0
                self.best_solution = new_best_solution
            else:
                self.improveless_iterations += 1

            self.iterations += 1
            

    
    def __mutate(self, chromosome : Solution):
        prob = random.uniform(0, 1)

        if self.mutation_probability >= prob:
            mutation_idx = random.randrange(0, len(self.mutations))
            print(mutation_idx)
            mutation = self.mutations[mutation_idx]
            new_chromosome = chromosome


            operation_count = random.randint(1, int(len(chromosome.state)*self.mutation_ops_percentage))
            for _ in range(0, operation_count):
                print("APPLYING MUTATION")
                new_chromosome = mutation(chromosome, self.simulation.duration)

            return new_chromosome
        
        return chromosome



    def __new_generation(self, population : List[Chromosome]):
        new_generation = [] if not self.elitism else sorted(population, reverse=True, \
                        key=lambda chromosome: chromosome.fitness)[:self.elitism_num]

        selection_num = self.population_size//2 if not self.elitism else self.population_size//2 - self.elitism_num

        for _ in range(selection_num):
            print("SELECTION")
            parent1, parent2 = self.selection_method.execute(population)      
            print("CROSSOVER")
            offspring1, offspring2 = self.crossover.execute(parent1.state, parent2.state)
            print("MUTATION")
            offspring1 = self.__mutate(offspring1)
            print("MUTATION2")
            offspring2 = self.__mutate(offspring2)
            chromosome1 = Chromosome(offspring1, self.simulation.run(offspring1))
            chromosome2 = Chromosome(offspring2, self.simulation.run(offspring2))
            new_generation.append(chromosome1)
            new_generation.append(chromosome2)

        return new_generation

    def get_solution(self) -> Solution:
        return self.best_solution.state

    def __get_best_solution(self, population: List[Chromosome]) -> Chromosome:
        return max(population, key=lambda chromosome: chromosome.fitness)

    def __random_population(self) -> List[Chromosome]:
        print("RANDOM POPULATION")
        population = []

        for _ in range(self.population_size):
            solution = Solution(self.simulation)
            solution.gen_random_solution(self.simulation.duration)
            population.append(Chromosome(solution, self.simulation.run(solution)))

        return population