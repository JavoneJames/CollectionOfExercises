import sys
from math import pow, sqrt, atan, degrees

from ex1 import ex1
from validation_handler import check_if_input_is_positive





def ex3():
    print("Enter two integers and calculate their binomial coefficients ")
    running = True
    while running:
        try:  # gets input from the user and checks if it is valid
            n = int(input("Enter the value of integer n: "))
            n = check_if_input_is_positive(n, "binomial_n")
            k = int(input("Enter the value of integer k: "))
            k = check_if_input_is_positive(k, "binomial_k")
            running = check_value_of_k(k, n)
        except ValueError:
            print(ValueError)


def ex4():
    running = True
    shortest_word = ""
    longest_word = ""
    while running:
        try:
            user_input = input("Please input a line of text: ").split()
            if len(user_input) == 0:
                raise IOError("Invalid input")
            for word in user_input:
                if len(shortest_word) == 0 or len(word.casefold()) < len(shortest_word.casefold()):
                    shortest_word = word
                if len(longest_word) == 0 or len(word) > len(longest_word.casefold()):
                    longest_word = word
                print(word)
            running = False
        except IOError as e:
            print(e)
            continue
    print(f"The length of the shortest word '{shortest_word}' is {len(shortest_word)}")
    print(f"The length of the shortest word '{longest_word}' is {len(longest_word)}")


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


def binomial(n, k):
    b = 1
    for i in range(min(k, n - k)):
        b *= n
        b //= i + 1
        n -= 1
    return b


def check_value_of_k(k, n):
    if k > n:
        print("When k > n the value is 0")
        print("This is because the n number must be larger or equal to k")
        running = False
    elif k == 1:
        print(f"The expression simplifies to {n}")
        print(f"In which n is {n} and k is {k}")
        running = False
    elif k == n or k == 0:
        print("The expression simplifies to 1")
        print(f"In which n is {n} and k is {k}")
        running = False
    else:
        result = binomial(n, k)
        print(f"The binomial coefficient of {n} and {k} is : {result}")
        running = False
    return running


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
