def sum_substring(start_indx, end_indx, string):
    chr_sum = 0
    if 0 <= start_indx in range(len(string)) and 0 <= end_indx in range(len(string)):
        substrg = string[start_indx:end_indx]
        for letter in substrg:
            chr_sum += int(ord(letter))
    else:
        return "Invalid indices!"

    return chr_sum


text = input()

command = input()

while command != 'Finish':
    action = command.split()[0]

    if action == "Replace":
        _, current_char, new_char = command.split()
        text = text.replace(current_char, new_char)
        print(text)
    elif action == 'Cut':
        start_index = int(command.split()[1])
        end_index = int(command.split()[2]) + 1

        if 0 <= start_index in range(len(text)) and 0 <= end_index in range(len(text)) and start_index < end_index:
            text = text[:start_index] + text[end_index:]
            print(text)
        else:
            print("Invalid indices!")
    elif action == 'Make':
        word_type = command.split()[1]
        if word_type == 'Upper':
            text = text.upper()
        elif word_type == 'Lower':
            text = text.lower()
        print(text)
    elif action == 'Check':
        substring = command.split()[1]
        if substring in text:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")
    elif action == 'Sum':
        start_i = int(command.split()[1])
        end_i = int(command.split()[2]) + 1

        print(sum_substring(start_i, end_i, text))

    command = input()