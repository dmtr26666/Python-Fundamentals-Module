budget = int(input())
bill = 0

while True:
    command = input()

    if command == 'End':
        print('You bought everything needed.')
        break
    else:
        price = int(command)
        bill += price

    if bill > budget:
        print('You went in overdraft!')
        break



