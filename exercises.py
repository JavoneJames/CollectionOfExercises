from math import pow, sqrt


def ex1():
    print("Exercise 1\n")
    running = True
    while running:
        try:  # prompt the user to input the height of the triangle - checks if it is positive
            triangle_height = float(input("Please enter the height of the triangle: "))
            triangle_height = check_if_input_is_positive(triangle_height, "height")
            # prompt the user to input the width of the triangle - checks if it is positive
            triangle_width = float(input("Please enter the width of the triangle: "))
            triangle_width = check_if_input_is_positive(triangle_width, "width")

        except ValueError as e:
            print(e)
        else:  # calculate the hypotenuse of the triangle and round it to 1dp - prints result to screen
            triangle_hypotenuse = round(sqrt(pow(triangle_height, 2) + pow(triangle_width, 2)), 1)
            print(f"The hypotenuse of the triangle  is {triangle_hypotenuse} cm\n")

#  checks if user input is a positive integer = if not prompts user to do so and then returns result
def check_if_input_is_positive(user_input, token):
    valid_input = 0
    if user_input < 0:
        running = True
        while running:
            print("Please enter a positive integer")
            valid_input = float(input(f"Please enter the {token} of the triangle: "))
            if valid_input > 0.0:
                running = False
    return valid_input


def select_exercise():
    list_of_exercises = [None, ex1]
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
