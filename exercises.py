from ex1 import ex1
from ex2 import ex2
from ex3 import ex3
from ex4 import ex4
from ex5 import ex5


def ex6():
    listOfNumbers = []
    running = True
    print("Enter a positive integer (- 1 integer to stop adding number to the list )")
    while running:
        try:
            user_input = int(input("Enter next number: "))
            if user_input < 0:
                running = False
                break
            listOfNumbers.append(user_input)
        except ValueError:
            print("Invalid input - Please enter a positive integer")
    bubble_sort(listOfNumbers)


def bubble_sort(listOfNumbers):
    if len(listOfNumbers) == 0:
        print("empty list")
        return
    elif len(listOfNumbers) <= 1:
        print(f"Only one element stored inside the list, which is: {listOfNumbers}")
        return
    print(f"The unsorted list looks like this: {listOfNumbers}")
    running = True
    while running:
        running = False
        for n in range(len(listOfNumbers) - 1):
            if listOfNumbers[n] > listOfNumbers[n + 1]:
                running = True
                temp = listOfNumbers[n]
                listOfNumbers[n] = listOfNumbers[n + 1]
                listOfNumbers[n + 1] = temp
    print(f"The sorted list looks like this: {listOfNumbers}")








def select_exercise():
    list_of_exercises = [None, ex1, ex2, ex3, ex4, ex5, ex6]
    running = True
    while running:
        line = input("Select an exercise (0 or 'q' to quit): ")
        if line == "0" or line == "q":
            running = False
        elif len(line) == 1 and "1" <= line <= "6":
            list_of_exercises[int(line)]()
        else:
            print("Invalid input - try again")


if __name__ == '__main__':
    select_exercise()
