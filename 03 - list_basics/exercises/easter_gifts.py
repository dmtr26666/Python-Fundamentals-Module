names_of_gifts = input().split()

while True:
    current_command = input().split()

    if 'Money' in current_command:
        break
    elif 'OutOfStock' in current_command:
        for element in names_of_gifts:
            if current_command[1] == element:
                names_of_gifts[names_of_gifts.index(current_command[1])] = 'None'
    elif 'Required' in current_command:
        if -1 < int(current_command[2]) <= len(names_of_gifts) - 1:
            names_of_gifts[int(current_command[2])] = current_command[1]
    elif 'JustInCase' in current_command:
        names_of_gifts[-1] = current_command[1]

for elem in names_of_gifts:
    if elem != 'None':
        print(elem, end=' ')

