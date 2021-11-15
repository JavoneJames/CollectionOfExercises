import datetime


def ex8():
    running = True
    while running:
        try:
            user_input =  input("Enter date in the following format (dd/mm/yyyy): ")
            if user_input == "":
                print("Invalid input")
                continue
            day, month, year = split_and_convert_input(user_input)
            check_if_date_is_valid(day, month, year)
            full_date = datetime.datetime(year, month, day)
            now = datetime.datetime.now()
            result = (full_date - now).days + 1
            print(f"The difference in date between {full_date.day}/{full_date.month}/{full_date.year} "
                  f"and {now.day}/{now.month}/{now.year} is: {result} days")
            running = False
        except ValueError as v:
            print(v)
            continue
        except Exception as e:
            print(f"Invalid input {e}")
            user_input = input("Would you like to try?: yes/no: ")
            if user_input.lower() == "yes":
                continue
            running = False


def split_and_convert_input(user_input):
    day, month, year = user_input.split('/')
    return int(day), int(month), int(year)


def check_if_date_is_valid(day, month, year):
    check_if_month_and_year_is_valid(day, month, year)
    check_for_leap_year_and_validate_feb_date(day, month, year)
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12 if day < 1 or day > 31:
            raise ValueError(f"Input for day is out of range, user input is {day}")
        case 4 | 6 | 9 | 11 if day < 1 or day > 30:
            raise ValueError(f"Input for day is out of range, user input is {day}")


def check_for_leap_year_and_validate_feb_date(day, month, year):
    if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0) and month == 2:
        print("leap year")
        if month == 2 and (day < 1 or day > 29):
            raise ValueError(f"Input for day is out of range, user input is {day}")
    elif month == 2 and (day < 1 or day > 28):
        raise ValueError(f"Input for day is out of range, user input is {day}")


def check_if_month_and_year_is_valid(day, month, year):
    if month < 1 or month > 12:
        raise ValueError(f"Input for month is out of range, user input is: {month}")
    current_year = datetime.datetime.now().year
    if year < current_year:
        raise ValueError(f"It's possible the date entered is in the past, please check {day}/{month}/{year}")