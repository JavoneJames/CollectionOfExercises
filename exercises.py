import sys


def ex1():
    pass


def select_exercise():
    list_of_exercises = [None, ex1]
    running = True
    while running:
        try:
            line = input("Select an exercise ( or 0/q to quit): ")
            if line == "0" or "q":
                running = False
            elif len(line) == 1 and "1" <= line <= "8":
                list_of_exercises[int(line)]()
            else:
                print("Invalid input - try again")
        except IOError:
            print("error")
    sys.exit(0)

if __name__ == '__main__':
    select_exercise()
