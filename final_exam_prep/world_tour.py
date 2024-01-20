def add_stop(index, destination, destination_list):
    if 0 <= index <= len(destination_list):
        for i in range(index, len(destination) + index):
            destination_list.insert(i, destination[i - index])
    return destination_list


def remove_stop(start_index, end_index, destination_list):
    if (0 <= start_index <= len(destination_list)) and end_index <= len(destination_list):
        del destination_list[start_index:end_index + 1]

    return destination_list


def switch(old_string, new_string, destination_list):
    whole_string = ''.join(destination_list)
    if old_string in whole_string:
        whole_string = whole_string.replace(old_string, new_string)

    destination_list = []
    for letter in whole_string:
        destination_list.append(letter)

    return destination_list


destinations = [x for x in input()]

while True:
    command = input()
    if command == "Travel":
        break

    command = command.split(':')
    action = command[0]

    if action == 'Add Stop':
        destinations = add_stop(int(command[1]), command[2], destinations)
    elif action == 'Remove Stop':
        destinations = remove_stop(int(command[1]), int(command[2]), destinations)
    elif action == 'Switch':
        destinations = switch(command[1], command[2], destinations)

    print(''.join(destinations))


print(f"Ready for world tour! Planned stops: {''.join(destinations)}")
