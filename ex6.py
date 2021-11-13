def ex6():
    listOfNumbers = []
    running = True
    print("Enter a positive integer (- 1 integer to stop adding number to the list )")
    while running:
        try:
            user_input = int(input("Enter next integer: "))
            if user_input < 0:
                running = False
                break
            listOfNumbers.append(user_input)
        except ValueError:
            print("Invalid input - Please enter a positive integer")
    list_validation(listOfNumbers)


def list_validation(listOfNumbers):
    if len(listOfNumbers) == 0:
        print("empty list")
        return
    elif len(listOfNumbers) <= 1:
        print(f"Only one element stored inside the list, which is: {listOfNumbers}")
        return
    print(f"The unsorted list looks like this: {listOfNumbers}")
    bubble_sort(listOfNumbers)
    print(f"The sorted list looks like this: {listOfNumbers}")


def bubble_sort(listOfNumbers):
    running = True
    while running:
        running = False
        for n in range(len(listOfNumbers) - 1):
            if listOfNumbers[n] > listOfNumbers[n + 1]:
                running = True
                temp = listOfNumbers[n]
                listOfNumbers[n] = listOfNumbers[n + 1]
                listOfNumbers[n + 1] = temp
