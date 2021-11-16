def check_if_input_is_positive(user_input, token):
    #  checks if user input is a positive integer = if not prompts user to do so and then returns result
    if user_input <= 0:
        running = True
        if token == "binomial_k" and user_input == 0:
            return 0
        while running:
            print("Please enter a positive integer")
            user_input = determine_message_to_be_shown(user_input, token)
            if user_input > 0.0:
                running = False
    return user_input


def determine_message_to_be_shown(user_input, token):
    match token:
        case "height" | "width":
            return float(input(f"Enter the {token} of the triangle: "))
        case "fibonacci":
            return int(input("How many numbers of the fibonacci sequence should be displayed? "))
        case "binomial_n":
            return int(input("Enter the value of integer n: "))
        case "binomial_k" if user_input < 0:
            return int(input("Enter the value of integer k: "))
        case "line of text":
            return input("Please input a line of text: ")
        case "rpw" | "column" :
            return int(input(f"Enter how many {token} you want to be displayed: "))