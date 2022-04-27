from email import message
import os
from select import select
from algorithms.algorithm_utils import gen_neighbour_lightOrOrder_func
from algorithms.chromosome import Chromosome
from algorithms.genetic import Genetic

from algorithms.hill_climbing import HillClimbing
from algorithms.iterated_local_search import IteratedLocalSearch
from algorithms.simulation import Simulation
from visualization import Visualization
import file_parsing
from algorithms.solution import Solution
from algorithms.hill_climbing import HillClimbing
from algorithms.simulated_annealing import SimulatedAnnealing
from algorithms.tabu import TabuSeach
from algorithms.simulation import Simulation
import file_parsing
from algorithms.algorithm_utils import gen_neighbour_lightOrOrder_func

import matplotlib.pyplot as plt
import time
from visualization import Visualization

class Menu:
    def __init__(self):
        self.print_welcome_message()

        self.current_menu = 0
        self.main_menu()

    def main_menu(self):
        options = {"1" : "Select input file" , "2" : "Run visualization", "3" : "Exit"}
        title = "Main Menu"
        message = "Select an option"
        self.print_menu(options,title, message)
        selected_option = self.select_option(1,3)

        if selected_option == 1:
            self.file_menu()
        elif selected_option == 2:
            self.visualization_menu()
        elif selected_option == 3:
            exit

    def file_menu(self):
        files = {"1": "a.txt", "2": "b.txt", "3": "c.txt", "4": "d.txt",
            "5": "e.txt", "6": "f.txt", "7": "Return to main menu"}
        title = "File Menu"
        message = "Choose an input file:"
        self.print_menu(files, title, message)
        selected_file = self.select_option(1,7)

        if selected_file == 7:
            self.main_menu()
        else:
            file = os.path.join('data','input', files[str(selected_file)])
            self.run_or_graph(file)
            self.algorithm_menu(file)

    ####################################################################################################################
    # ALGORITHMS

    def run_or_graph(self,file):
        options = {"1" : "Run Algorithm", "2" : "See Algorithm's Quality Plot" , "3" : "Go Back to Main Menu", "4" : "Exit"}
        title = "Run or Show Plot"
        message =  "Select an option"
        self.print_menu(options,title, message)
        selected_option = self.select_option(1,4)
        
        if selected_option == 1:
            self.run_algorithm_menu(file)
        elif selected_option == 2:
            self.show_plot_menu(file)
        elif selected_option == 3:
            self.main_menu()
        elif selected_option == 4:
            exit()
    
    def run_algorithm_menu(self,file):
        algortihms = {"1": "Greeedy", "2" : "Hill Climbing", "3" : "Simulated Annealing" , "4" : "Genetic" , "5" : "Iterative Search", "6" : "Tabu Search", "7" : "Go Back to Main Menu", "8" : "Exit"}
        title = "Algorithm Menu"
        message =  "Select an algorithm"
        self.print_menu(algortihms,title, message)
        selected_algorithm = self.select_option(1,8)

        if selected_algorithm == 1:
            self.run_greedy(file)
            self.run_after_algorithm()
        if selected_algorithm == 2:
            self.run_hill_climbing(file)
            self.run_after_algorithm()
        elif selected_algorithm == 3:
            self.run_simulated_annealing(file)
            self.run_after_algorithm()
        elif selected_algorithm == 4:
            self.run_genetic(file)
            self.run_after_algorithm()
        elif selected_algorithm == 5:
            self.run_iterative_search(file)
            self.run_after_algorithm()
        elif selected_algorithm == 6:
            self.run_tabu_search(file)
            self.run_after_algorithm()
        elif selected_algorithm == 7:
            self.main_menu()
        elif selected_algorithm == 8:
            exit()

    def show_plot_menu(self,file):
        algortihms = {"1" : "Hill Climbing", "2" : "Simulated Annealing" , "3" : "Tabu Search", "4" : "Go Back to Main Menu", "5" : "Exit"}
        title = "Plot Menu"
        message =  "Selec an algorithm"
        self.print_menu(algortihms,title, message)
        selected_algorithm = self.select_option(1,5)

        if selected_algorithm == 1:
            self.run_hill_climbing(file,True)
            self.run_after_algorithm()
        elif selected_algorithm == 2:
            self.run_simulated_annealing(file,True)
            self.run_after_algorithm()
        elif selected_algorithm == 3:
            self.run_tabu_search(file,True)
            self.run_after_algorithm()
        elif selected_algorithm == 4:
            self.main_menu()
        elif selected_algorithm == 5:
            exit()

    def run_greedy(self,file):
        sim_duration, points_per_car, intersections, streets, cars = file_parsing.parse(file)
        simulation = Simulation(sim_duration, points_per_car, intersections, streets, cars)

        sol = Solution(simulation)
        start = time.time()
        sol.gen_greedy_solution()
        end = time.time()
        print(f'Points: {simulation.run(sol)}')
        print(f'time: {end-start}')

    def run_hill_climbing(self,file,plot=False):
        sim_duration, points_per_car, intersections, streets, cars = file_parsing.parse(file)
        simulation = Simulation(sim_duration, points_per_car, intersections, streets, cars)

        hill_climbing = HillClimbing(simulation)
        neighbour_func = gen_neighbour_lightOrOrder_func(50, 3)
        all_points = hill_climbing.execute(neighbour_func)
        _, bestPoints = hill_climbing.get_solution()

        if plot:
            plt.plot(all_points, 'o-', markersize=3)
            plt.ylabel("Best Solution's Points")
            plt.show()
        else:
            print("Points: ", bestPoints)

    
    def run_simulated_annealing(self,file,plot=False):
        sim_duration, points_per_car, intersections, streets, cars = file_parsing.parse(file)
        simulation = Simulation(sim_duration, points_per_car, intersections, streets, cars)

        simulated_annealing = SimulatedAnnealing(simulation)
        sol = Solution(simulation)
        sol.gen_greedy_solution()
        #sol.gen_random_solution(10)
        neighbour_func = gen_neighbour_lightOrOrder_func(50, 3)


        random_solution = sol.copy()
        start = time.time()
        all_points = simulated_annealing.execute(0.01, 0, neighbour_func, random_solution)
        end = time.time()

        _, bestPoints = simulated_annealing.get_solution()
        
        if plot:
            plt.plot(all_points, 'o-', markersize=3)
            plt.ylabel("Best Solution's Points")
            plt.show()
        else:
            print("Elapsed time: ", end - start)
            print("Points: ", bestPoints)

    
    def run_genetic(self, file):
        sim_duration, points_per_car, intersections, streets, cars = file_parsing.parse(file)
        simulation = Simulation(sim_duration, points_per_car, intersections, streets, cars)

        start_population = []
        for i in range(100):
            solution = gen_neighbour_lightOrOrder_func(50, simulation.duration)
            p = simulation.evaluate_solution(None, solution)
            start_population.append(Chromosome(solution, p))
        genetic_utils = Genetic(simulation, max_improveless_iterations=None, max_iterations=50, population_size=100, elitism_num=20,mutation_probability=0.4, mutation_ops_percentage=0.1)
        genetic_utils.execute(start_population)
        simulation.evaluate_solution(None, genetic_utils.get_solution())

    
    def run_iterative_search(self,file):
        sim_duration, points_per_car, intersections, streets, cars = file_parsing.parse(file)
        simulation = Simulation(sim_duration, points_per_car, intersections, streets, cars)

        iter = IteratedLocalSearch(simulation)
        sol = Solution(simulation)
        sol.gen_greedy_solution()
        points = simulation.run(sol)

        start = time.time()
        solution, best_points = iter.execute( gen_neighbour_lightOrOrder_func(50, simulation.duration), start_solution=sol, start_points=points)
        end = time.time()
        print(f'points: {best_points}')
        print(f'time: {end - start}')

    def run_tabu_search(self,file,plot=False):
        sim_duration, points_per_car, intersections, streets, cars = file_parsing.parse(file)
        simulation = Simulation(sim_duration, points_per_car, intersections, streets, cars)

        tabu_search = TabuSeach(simulation)
        sol = Solution(simulation)
        sol.gen_greedy_solution()
        neighbour_func = gen_neighbour_lightOrOrder_func(50, 3)
        start = time.time()
        best_cand_points = tabu_search.execute(20, neighbour_func, sol)
        end = time.time()

        _, bestPoints = tabu_search.get_solution()

        if plot:
            plt.plot(best_cand_points, 'o-', markersize=3)
            plt.ylabel("Points")
            plt.show()
        else: 
            print("Elapsed time: ", end - start)
            print("Best points obtained: ", bestPoints)

    def run_after_algorithm(self):
        options = {"1" : "Go Back to Main Menu", "2" : "Exit"}
        title = "What Now?"
        message = "Select an option"
        self.print_menu(options,title, message)
        selected_option = self.select_option(1,2)

        if selected_option == 1:
            self.main_menu()
        elif selected_option == 2:
            exit()

    ####################################################################################################################

    def visualization_menu(self):
        sim_duration, points_per_car, intersections, streets, cars = file_parsing.parse("data/input/a.txt")
        simulation = Simulation(sim_duration, points_per_car, intersections, streets, cars)

        bestPoints = 0
        while(bestPoints < 2000):
            hill_climbing = HillClimbing(simulation)
            neighbour_func = gen_neighbour_lightOrOrder_func(50, 3)
            hill_climbing.execute(neighbour_func)
            bestSol, bestPoints = hill_climbing.get_solution()

        visualization = Visualization(simulation.intersections, simulation.streets, simulation.cars)

        simulation.run_visualization(visualization, bestSol)
     
    def select_option(self,min_value, max_value):
        user_input = input("Insert a number from the menu: \n")
        while True:
            try:
                val = int(user_input)
                if val < min_value or val > max_value:
                    user_input = input("Invalid input, please insert a valid one: ")
                else:
                    break
            except ValueError:
                user_input = input("Invalid input, please insert a valid one: ")

        return val

    def print_menu(self,options,title,message):
        print("=============================================")
        print("               ", title)
        print("---------------------------------------------")
        print(message, '\n')

        for key, value in options.items():
            print(key + ". " + value)
        print("=============================================")

    
    def print_welcome_message(self):
        print("")
        print("")
        print(" \ \        / /  ____| |    / ____/ __ \|  \/  |  ____|")
        print("  \ \  /\  / /| |__  | |   | |   | |  | | \  / | |__   ")
        print("  \ \  /\  / /| |__  | |   | |   | |  | | \  / | |__ ")
        print("   \ \/  \/ / |  __| | |   | |   | |  | | |\/| |  __|  ")
        print("    \  /\  /  | |____| |___| |___| |__| | |  | | |____ ")
        print("     \/  \/   |______|______\_____\____/|_|  |_|______|")
        print("")
        print("")