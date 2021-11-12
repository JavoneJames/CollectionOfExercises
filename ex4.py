def ex4():
    running = True
    shortest_word = ""
    longest_word = ""
    while running:
        try:
            user_input = input("Please input a line of text: ").split()
            if len(user_input) == 0:
                print("Invalid input")
                continue
            print(f"String input from the user \"{user_input}\"")
            longest_word, running, shortest_word = figure_out_which_is_shortest_and_longest(longest_word, shortest_word, user_input)
        except IOError as e:
            print(e)
    print(f"The length of the shortest word '{shortest_word}' is {len(shortest_word)}")
    print(f"The length of the shortest word '{longest_word}' is {len(longest_word)}")


def figure_out_which_is_shortest_and_longest(longest_word, shortest_word, user_input):
    for word in user_input:
        if len(shortest_word) == 0 or len(word.casefold()) < len(shortest_word.casefold()):
            shortest_word = word
        if len(longest_word) == 0 or len(word) > len(longest_word.casefold()):
            longest_word = word
        print(word)
    running = False
    return longest_word, running, shortest_word
