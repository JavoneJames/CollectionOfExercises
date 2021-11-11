import sys
from math import pow, sqrt, atan, degrees


def ex1():
    print("Exercise 1 - Get the height and width of a right-angled triangle "
          "then work out the degrees of the other two angles\n")
    running = True
    while running:
        try:  # prompt the user to input the height of the triangle - checks if it is positive
            triangle_height = float(input("Please enter the height of the triangle: "))
            triangle_height = check_if_input_is_positive(triangle_height, "height")
            # prompt the user to input the width of the triangle - checks if it is positive
            triangle_width = float(input("Please enter the width of the triangle: "))
            triangle_width = check_if_input_is_positive(triangle_width, "width")
            running = False
        except ValueError as e:
            print(e)
        else:  # calculate the hypotenuse of the triangle and round it to 1dp - prints result to screen
            triangle_hypotenuse = round(sqrt(pow(triangle_height, 2) + pow(triangle_width, 2)), 1)
            print(f"The hypotenuse of the triangle  is {triangle_hypotenuse} cm")
            #  divide height and width to calculate the radian
            radian = atan(triangle_height / triangle_width)
            #  converts radian to degrees 1dp
            degree_of_angle_a = round(degrees(radian), 1)
            print(f"The angle of A is : {degree_of_angle_a}\u0080")
            #  get the degree of the other unknown angle by subtracting right angle by angle A
            degree_of_angle_b = round(90 - degree_of_angle_a, 1)
            print(f"The angle of B is : {degree_of_angle_b}\u0080")


def ex2():  # prompts user for input - then checks if the input is valid
    print("Exercise 2 - Enter a number and display all the fibonacci sequence to that nth")
    user_input = int(input("How many numbers of the fibonacci sequence should be displayed? "))
    user_input = check_if_input_is_positive(user_input, "fibonacci")
    first_number = 0
    second_number = 1
    #  swap numbers to be printed and calculate the sum of the next number in the sequence
    if user_input == 0: return print(0)
    while user_input > 0:
        print_value = first_number
        first_number = second_number
        second_number = print_value + second_number
        user_input = user_input - 1
        if user_input != 0:
            print(print_value, end=', ')
        else:
            print(print_value)
    print("\n")


def ex3():
    print("Enter two integers and calculate their binomial coefficients ")
    running = True
    while running:
        try:
            n = int(input("Enter the value of integer n: "))
            n = check_if_input_is_positive(n, "binomial_x")
            k = int(input("Enter the value of integer k: "))
            k = check_if_input_is_positive(k, "binomial_y")
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


def check_if_input_is_positive(user_input, token):
    #  checks if user input is a positive integer = if not prompts user to do so and then returns result
    if user_input < 0:
        running = True
        while running:
            print("Please enter a positive integer")
            user_input = determine_message_to_be_shown(token)
            if user_input > 0.0:
                running = False
    return user_input


def determine_message_to_be_shown(token):
    match token:
        case "height" | "width":
            return float(input(f"Please enter the {token} of the triangle: "))
        case "fibonacci":
            return int(input("How many numbers of the fibonacci sequence should be displayed? "))
        case "binomial_x":
            return int(input("Enter the value of integer x: "))
        case "binomial_y":
            return int(input("Enter the value of integer y: "))
        case "line of text":
            return input("Please input a line of text: ")

def binomial(n, k):
    b = 1
    for i in range(min(k, n - k)):
        b *= n
        b //= i + 1
        n -= 1
    return b


def select_exercise():
    list_of_exercises = [None, ex1, ex2, ex3, ex4]
    running = True
    while running:
        line = input("Select an exercise (0 or 'q' to quit): ")
        if line == "0" or line == "q":
            running = False
        elif len(line) == 1 and len(line) <= 4:
            list_of_exercises[int(line)]()
        else:
            print("Invalid input - try again")


if __name__ == '__main__':
    select_exercise()
