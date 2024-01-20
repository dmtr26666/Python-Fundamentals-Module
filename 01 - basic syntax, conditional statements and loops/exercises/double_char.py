while True:
    string = input()

    if string == 'End':
        break
    elif string == 'SoftUni':
        continue

    for i in range(len(string)):
        print(string[i] * 2, end='')

    print()