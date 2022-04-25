from email import message
from select import select


class Menu:
    def main_menu(self):
        options = {"1" : "Select input file" , "2" : "Run visualization" , "3" : "Exit"}
        title = "Main Menu"
        message = "Select an option"
        chosen_option = self.print_menu(options, title, message)

        if chosen_option == 3:
            return -1
        return chosen_option

    def file_menu(self):
        files = {"1": "a.txt", "2": "b.txt", "3": "c.txt", "4": "d.txt",
            "5": "e.txt", "6": "f.txt", "7": "Return to main menu"}
        title = "File Menu"
        message = "Choose an input file:"
        chosen_option = self.print_menu(files, title, message)

        if chosen_option == 7:
            return 0
        return files[str(chosen_option)]

    def algorithm_menu(self,file):
        algortihms = {"1" : "Hill Climbing", "2" : "Simulated Annealing" , "3" : "Genetic" , "4" : "Exit"}
        title = "Algorithm Menu"
        message =  "Selec which algorithm you want to run"
        chosen_algorithm = self.print_menu(algortihms,title, message)

    def menu(self):
        current_menu = 0
        input_file = "a.txt"

        while current_menu != -1:

            # main menu
            if current_menu == 0:
                current_menu = self.main_menu()
            
            # file menu
            elif current_menu == 1:
                current_menu = self.file_menu()

            #  algorithm menu
            elif current_menu == 3:
                current_menu = self.algorithm_menu(input_file)
    
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

        return self.select_option(1, len(options))
    


menu = Menu()
menu.main_menu()