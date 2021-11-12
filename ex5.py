def ex5():
    running = True
    vowels = "aeiou"
    store_occurrence_of_vowels = {}
    while running:
        try:
            user_input = input("Please input a line of text: ")
            if len(user_input) == 0:
                raise IOError("Invalid input")
            print(f"The following line was inputted by the user: \"{user_input}\"")
            check_for_vowels_in_line(store_occurrence_of_vowels, user_input, vowels)
            if not bool(store_occurrence_of_vowels):
                return print("no vowels found in the line of text")
            print(f"visual display of all the vowels found within the text: {store_occurrence_of_vowels}")
            print("The least occurring vowel(s) from the text is; ", end='')
            running = display_occurrences_of_vowels(store_occurrence_of_vowels)
        except IOError as e:
            print(e)


def display_occurrences_of_vowels(store_occurrence_of_vowels):
    for occ in store_occurrence_of_vowels:
        if store_occurrence_of_vowels[occ] == min(store_occurrence_of_vowels.values()):
            print(f"{occ} with {store_occurrence_of_vowels[occ]} occurrences")
    return False


def check_for_vowels_in_line(store_occurrence_of_vowels, user_input, vowels):
    for char in user_input.casefold():
        if char in vowels:
            if char not in store_occurrence_of_vowels:
                store_occurrence_of_vowels[char] = 1
            else:
                store_occurrence_of_vowels[char] += 1
