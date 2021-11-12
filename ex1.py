from validation_handler import check_if_input_is_positive
from math import pow, sqrt, atan, degrees


def ex1():
    print("Exercise 1 - Get the height and width of a right-angled triangle "
          "then work out the degrees of the other two angles\n")
    running = True
    triangle_height = ""
    triangle_width = ""
    while running:
        try:  # prompt the user to input the height of the triangle - checks if it is positive
            triangle_height = float(input("Enter the height of the triangle: "))
            triangle_height = check_if_input_is_positive(triangle_height, "height")
            # prompt the user to input the width of the triangle - checks if it is positive
            triangle_width = float(input("Enter the width of the triangle: "))
            triangle_width = check_if_input_is_positive(triangle_width, "width")
            running = False
        except ValueError as e:
            print(e)
    calculate_degree_of_other_angles(triangle_height, triangle_width)


def calculate_degree_of_other_angles(triangle_height, triangle_width):
    # calculate the hypotenuse of the triangle and round it to 1dp - prints result to screen
    triangle_hypotenuse = round(sqrt(pow(triangle_height, 2) + pow(triangle_width, 2)), 1)
    print("")
    print(f"The hypotenuse of the triangle is {triangle_hypotenuse}cm")
    #  divide height and width to calculate the radian
    radian = atan(triangle_height / triangle_width)
    #  converts radian to degrees 1dp
    degree_of_angle_a = round(degrees(radian), 1)
    print(f"The angle of A is : {degree_of_angle_a}\u0080")
    #  get the degree of the other unknown angle by subtracting right angle by angle A
    degree_of_angle_b = round(90 - degree_of_angle_a, 1)
    print(f"The angle of B is : {degree_of_angle_b}\u0080")
