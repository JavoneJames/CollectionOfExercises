def ex10():
    running = True
    while running:
        try:
            user_input = input("Enter a string to be encrypted: ")
            if not user_input:
                raise IOError("Invalid empty input - try again")
            if user_input.isdigit():
                raise IOError("Invalid numeric only input - try again ")
            encryption_key = int(input("Enter encryption key: "))
            if encryption_key < 1:
                raise ValueError("Invalid negative integer input - try again")
            encryption_handler(user_input, encryption_key)
        except IOError as io:
            print(io)
            continue
        except ValueError as v:
            print(v)
            continue
        except Exception as e:
            print(e)

def encryption_handler(user_input, key):
    temp_list = []
    for i in range(len(user_input)):
        char = user_input[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + key-65) % 26 + 65)
        else:
            encrypted_char = chr((ord(char) + key-97) % 26 + 97)
        temp_list.append(encrypted_char)
        print(encrypted_char, end='')
    print()


