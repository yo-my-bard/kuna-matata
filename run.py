import sys
import os

class KunaMatata:
    
    def __init__(self):
        self.menu_options = {'1': "Create a new problem",
                        '2': "Add a new solution attempt",
                        '3': "Review all existing attempts",
                        '4': "Save existing attempts to .txt file",
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
                if k in ['2', '3', '4']:
                    continue
                allowed_options.append(k)
                print(k, '\t', v)
            else:
                if k in ['1']:
                    print(f'Currently working on: {self.problem.prob}')
                    continue
                allowed_options.append(k)
                print(k, '\t', v)
        
        self.listen_for_option(allowed_options)
    
    def listen_for_option(self, allowed_options):
        opt = input("Select an option: ")
        self.handle_option(opt, allowed_options)
        return opt

    def handle_option(self, opt, allowed_options):
        handle = {'1': lambda: self.create_new_problem(),
                 '2': lambda: self.add_solution_attempt(),
                 '3': lambda: self.print_attempts(),
                 '4': lambda: self.save_attempts(),
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
        response = input("\nDetail the latest attempt (type :back to return to menu): ")
        if response == ":back":
            self.print_menu()
        else:
            self.problem.attempts.append(response)
            print()
            self.print_menu()
    
    def print_attempts(self):
        if self.problem.attempts:
            for n, attempt in enumerate(self.problem.attempts):
                print(f'Attempt #{n+1}', '\t', attempt, '\n')
        else:
            print("Every journey begins with the first step, and ya ain't done that yet!\n")
        
        self.print_menu()
    
    def save_attempts(self, fmt='txt', fname='output'):
        os.makedirs("output", exist_ok=True)

        if self.problem.attempts and fmt=='txt':
            with open(f'./output/{fname}.txt', 'w') as f:
                for n, attempt in enumerate(self.problem.attempts):
                    f.write(f"Attempt {n+1}:\t")
                    f.write(attempt)
                    if n < len(self.problem.attempts) - 1:
                        f.write('\n')
                f.close()
        else:
            print("No existing attempts to save! Try adding an attempt first.\n")
            self.print_menu()
    


class Problem:

    def __init__(self, prob=None, attempts=[]):
        self.prob = prob
        self.attempts = attempts

    def get_problem(self, prob=None):
        print()
        self.prob = input("What's the problem we're solving today? ") 
        print()


if __name__ == '__main__':
    KunaMatata()