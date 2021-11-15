from ex1 import ex1
from ex2 import ex2
from ex3 import ex3
from ex4 import ex4
from ex5 import ex5
from ex6 import ex6
from ex7 import ex7
from ex8 import ex8


def select_exercise():
    list_of_exercises = [None, ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8]
    running = True
    while running:
        line = input("Select an exercise (0 or 'q' to quit): ")
        if line == "0" or line == "q":
            running = False
        elif len(line) == 1 and "1" <= line <= "8":
            list_of_exercises[int(line)]()
        else:
            print("Invalid input - try again")


if __name__ == '__main__':
    select_exercise()
