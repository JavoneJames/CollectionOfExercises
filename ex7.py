def ex7():
    running = True
    while running:
        try:
            user_input = int(input("Enter an integer: "))
            if user_input < 2 or str(user_input) == 0:
                print("Invalid input")
                if user_input == 1:
                    print(f"Btw the integer {user_input} is not a prime number, you know that right?")
                continue
            if user_input in range(4):
                print(f"{user_input} is a prime integer")
            check_for_prime(user_input)
            running = False
        except ValueError as v_error:
            print(v_error)


def check_for_prime(user_input):
    for i in range(2, user_input):
        if user_input % i == 0:
            print(f"{user_input} is not a prime number")
            break
        else:
            print(f"{user_input} is a prime number")
            break
