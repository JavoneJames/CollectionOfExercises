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


def binomial(n, k):
    b = 1
    for i in range(min(k, n - k)):
        b *= n
        b //= i + 1
        n -= 1
    return b
