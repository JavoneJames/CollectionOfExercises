import sys
from math import pow, sqrt, atan, degrees

from ex1 import ex1
from ex2 import ex2
from ex3 import ex3
from ex4 import ex4
from validation_handler import check_if_input_is_positive










def ex5():
    running = True
    vowels = "aeiou"
    store_occurrence_of_vowels = {}
    while running:
        try:
            user_input = input("Please input a line of text: ")
            if len(user_input) == 0:
                raise IOError("Invalid input")
            print(f"The following line was inputted by the user: \"{user_input}\"")
            for char in user_input.casefold():
                if char in vowels:
                    if char not in store_occurrence_of_vowels:
                        store_occurrence_of_vowels[char] = 1
                    else:
                        store_occurrence_of_vowels[char] += 1
            if not bool(store_occurrence_of_vowels):
                return print("no vowels found in the line of text")
            print(f"visual display of all the vowels found within the text: {store_occurrence_of_vowels}")
            print("The least occurring vowel(s) from the text is; ", end='')
            for occ in store_occurrence_of_vowels:
                if store_occurrence_of_vowels[occ] == min(store_occurrence_of_vowels.values()):
                    print(f"{occ} with {store_occurrence_of_vowels[occ]} occurrences")
            running = False
        except IOError as e:
            print(e)


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
