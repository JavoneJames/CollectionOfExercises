from validation_handler import check_if_input_is_positive


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
