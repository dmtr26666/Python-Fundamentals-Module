def numbers_between(a, b):
    char_list = [chr(i) for i in range(ord(a) + 1, ord(b))]

    string = ' '.join(char_list)
    return string


starting_char = input()
ending_char = input()

print(numbers_between(starting_char, ending_char))
