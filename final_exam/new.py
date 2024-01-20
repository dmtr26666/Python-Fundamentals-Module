def replace(current_char, new_char, string):
    string = string.replace(current_char, new_char)
    return string


def cut(start_index, end_index, string):
    string = string[:start_index] + string[end_index + 1:]
    return string


def make(state, string):
    if state == 'Upper':
        string = string.upper()
    elif state == 'Lower':
        string = string.lower()

    return string


def sum_substring(start_indx, end_indx, string):
    chr_sum = 0
    if 0 <= start_indx <= len(string) and 0 <= end_indx <= len(string):
        substrg = string[start_indx:end_indx]
        for letter in substrg:
            chr_sum += int(ord(letter))
    else:
        return "Invalid indices!"

    return chr_sum


initial_string = input()

while True:
    command = input()
    if command == 'Finish':
        break

    action = command.split()[0]

    if action == 'Replace':
        curr_char = command.split()[1]
        new_char = command.split()[2]
        initial_string = replace(curr_char, new_char, initial_string)
        print(initial_string)
    elif action == 'Cut':
        start_i = int(command.split()[2])
        end_i = int(command.split()[1])
        if 0 <= start_i <= len(initial_string) and 0 <= end_i <= len(initial_string):
            initial_string = cut(start_i, end_i, initial_string)
            print(initial_string)
        else:
            print("Invalid indices!")
    elif action == 'Make':
        state = command.split()[1]
        initial_string = make(state, initial_string)
        print(initial_string)
    elif action == 'Check':
        to_check = command.split()[1]

        if to_check in initial_string:
            print(f"Message contains {to_check}")
        elif to_check not in initial_string:
            print(f"Message doesn't contain {to_check}")
    elif action == 'Sum':
        start_i = int(command.split()[2])
        end_i = int(command.split()[1]) + 1

        print(sum_substring(start_i, end_i, initial_string))

