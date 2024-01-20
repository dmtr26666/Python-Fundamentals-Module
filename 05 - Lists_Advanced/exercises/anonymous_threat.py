from math import floor

def merge(list, startindex, endindex):
    elements = list[startindex:endindex + 1]
    merged_elements = ''.join(elements)

    if startindex not in range(len(list) - 1):
        startindex = 0
    if endindex not in range(len(list) - 1):
        endindex = len(list) - 1

    del list[startindex + 1:endindex + 1]
    list[startindex] = merged_elements


    return list


def divide(list, index, partitions):
    word = list.pop(index)
    letters_per_partition = floor(len(word) / partitions)

    last_index = 0

    for i in range(partitions):
        if i == partitions - 1:
            list.insert(index, word[last_index:])
        else:
            list.insert(index, word[last_index:last_index + letters_per_partition])
        index += 1
        last_index += letters_per_partition

    return list


string_as_list = input().split()
command = input()

while command != '3:1':
    command = command.split()
    operation = command[0]

    if operation == 'merge':
        string_as_list = merge(string_as_list, int(command[1]), int(command[2]))

    elif operation == 'divide':
        string_as_list = divide(string_as_list, int(command[1]), int(command[2]))

    command = input()
else:
    print(' '.join(string_as_list))