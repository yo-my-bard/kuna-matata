import sys
import os
import re

class KunaMatata:
    
    def __init__(self):
        self.menu_options = {'1': "Create a new problem",
                        '2': "Add a new solution attempt",
                        '3': "Review all existing attempts",
                        '4': "Save existing attempts to .txt file",
                        '5': "Load previous problem and attempts",
                        '0': "Exit"}
        self.introduction = "Welcome to Kuna Matata. It's Kiswahili for 'there are problems'.\
            \nAnd indeed, there are problems and this script is meant to help to track all of the\
            \nattempted solutions that fail before you find the one that works!\n"
        
        self.problem = None
        print(self.introduction)
        self.print_menu()

    def print_menu(self):
        allowed_options = []
        print("\nSelect an option:")
        for k,v in self.menu_options.items():
            if not self.problem:
                if k in ['2', '3', '4']:
                    continue
                allowed_options.append(k)
                print(k, v)
            else:
                if k in ['1']:
                    print(f'Currently working on: {self.problem.prob}')
                    continue
                allowed_options.append(k)
                print(k, v)
        
        self.listen_for_option(allowed_options)
    
    def listen_for_option(self, allowed_options):
        opt = input("Select an option (one of the numbers above): ")
        if opt == '4':
            suboption = input("Name for your output .txt file? (Press Enter for default output.txt. Weird file names will cause an error ¯\_(ツ)_/¯) ")
            self.handle_option(opt, allowed_options, suboption)
        elif opt == '5':
            suboption = input("Path to the .txt file that you are trying to load? ")
            self.handle_option(opt, allowed_options, suboption)
        self.handle_option(opt, allowed_options)
        return opt

    def handle_option(self, opt, allowed_options, suboption=None):
        handle = {'1': lambda: self.create_new_problem(),
                 '2': lambda: self.add_solution_attempt(),
                 '3': lambda: self.print_attempts(),
                 '4': lambda: self.save_attempts(fname=suboption),
                 '5': lambda: self.load_attempt(fname=suboption),
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
        if not fname.strip():
            fname='output'
        if self.problem.attempts and fmt=='txt':
            with open(f'./output/{fname}.txt', 'w') as f:
                f.write(f"Problem statement: {self.problem.prob}\n")
                for n, attempt in enumerate(self.problem.attempts):
                    f.write(f"Attempt {n+1}:\t")
                    f.write(attempt)
                    if n < len(self.problem.attempts) - 1:
                        f.write('\n')
                f.close()
            self.print_menu()
        else:
            print("No existing attempts to save! Try adding an attempt first.\n")
            self.print_menu()
    
    def load_attempt(self, fmt='txt', fname='./output/output.txt'):
        try:
            with open(fname, 'r') as f:
                prob_statement = f.readline()
                prob_statement = prob_statement.split('Problem statement: ')[1].strip()
                self.problem = Problem()
                self.problem.prob = prob_statement

                while True:
                    line = f.readline()
                    if line:
                        assert 'Attempt' in line, "Unexpected formatting in .txt file"
                        new_line = re.split('Attempt .+\\t', line)[1].strip()
                        self.problem.attempts.append(new_line)
                    else:
                        break
            print(f"Successfully loaded file from {fname}.")
            self.print_menu()
        except FileNotFoundError:
            print("Try different file name")
            self.print_menu()
    
class Problem:

    def __init__(self, prob=None, attempts=None):
        self.prob = prob
        if not attempts:
            self.attempts = []
        else:
            self.attempts = attempts

    def get_problem(self, prob=None):
        print()
        self.prob = input("What's the problem we're solving today? ") 
        print()


if __name__ == '__main__':
    KunaMatata()