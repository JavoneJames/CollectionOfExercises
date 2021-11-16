from validation_handler import check_if_input_is_positive
def ex9():
    running = True
    while running:
        try:
            row  = int(input("How many rows do you want to be displayed?: "))
            check_if_input_is_positive(row, "row")
            column = int(input("How many columns do you want to be displayed?: "))
            check_if_input_is_positive(column, "column")
            for r in range(1, row + 1):
                for c in range(1, column + 1):
                    print(("{:>{}}".format(r ** c, column)), end=" ")
                print()
        except ValueError as v:
            print(v)
            continue
        except Exception as e:
            print(e)
