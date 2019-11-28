import sys

class Menu:
    
    def __init__(self):
        self.menu_options = {'1': "Create a new problem",
                        '2': "Add a new solution attempt",
                        '0': "Exit"}
        self.introduction = "Welcome to Kuna Matata. It's Swahili for 'there are problems'.\
            \nAnd indeed, there are problems that need solving. Use this to track all of the\
            \nattempts that fail before you find the one that works!\n"
        
        self.problem = None
        
        print(self.introduction)
        self.print_menu()

    def print_menu(self):
        print("Select an option:")
        allowed_options = []
        for k,v in self.menu_options.items():
            if not self.problem:
                if k in ['2']:
                    continue
                allowed_options.append(k)
                print(k, '\t', v)
            else:
                if k in ['1']:
                    print(f'\nCurrently working on: {self.problem.prob}')
                    continue
                allowed_options.append(k)
                print(k, '\t', v)
        
        self.listen_for_option(allowed_options)
    
    def listen_for_option(self, allowed_options):
        opt = input("Select an option: ")
        self.handle_option(opt, allowed_options)
        return opt

    def reprompt(self):
        self.print_menu()
        # self.listen_for_option(allowed_options)

    def handle_option(self, opt, allowed_options):
        handle = {'1': lambda: self.create_new_problem(),
                 '2': lambda: self.add_solution_attempt(),
                 '0': sys.exit}
        if opt not in allowed_options:
            print(f"\nSelected option, {opt}, not allowed. Try again.")
            self.listen_for_option(allowed_options)
        handle[opt]()

    def create_new_problem(self):
        self.problem = Problem()
        self.problem.get_problem()
        self.print_menu()

    def add_solution_attempt(self):
        self.problem.attempts.append(input("\nDetail the latest attempt: "))
        print(self.problem.attempts)
        self.print_menu()
    


class Problem:

    def __init__(self, prob=None, attempts=[]):
        self.prob = prob
        self.attempts = attempts

    def get_problem(self, prob=None):
        print()
        self.prob = input("What's the problem we're solving today? ") 
        print()

m = Menu()