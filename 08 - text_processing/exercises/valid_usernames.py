usernames = input().split(', ')

valid_name = []


for name in usernames:
    valid = True
    if 3 <= len(name) <= 16:
        for letter in name:
            if letter.isdigit() == False and letter.isalpha() == False and letter != '-' and letter != '_':
                valid = False
                break

        if valid:
            valid_name.append(name)

print('\n'.join(valid_name))