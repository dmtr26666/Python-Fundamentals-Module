number_of_wagons = int(input())

wagons = [0] * number_of_wagons

while True:
    command = input().split()

    if command[0] == 'End':
        print(wagons)
        break
    elif command[0] == 'add':
        value = int(command[1])
        wagons[-1] += value
    elif command[0] == 'insert':
        index = int(command[1])
        value = int(command[2])
        wagons[index] += value
    elif command[0] == 'leave':
        index = int(command[1])
        value = int(command[2])
        wagons[index] -= value

