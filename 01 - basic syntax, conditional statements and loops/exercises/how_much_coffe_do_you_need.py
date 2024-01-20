total_coffes = 0

while True:
    event = input()

    if event == 'END':
        break

    if event == 'coding':
        total_coffes += 1
    elif event == 'CODING':
        total_coffes += 2
    elif event == 'cat':
        total_coffes += 1
    elif event == 'CAT':
        total_coffes += 2
    elif event == 'dog':
        total_coffes += 1
    elif event == 'DOG':
        total_coffes += 2
    elif event == 'movie':
        total_coffes += 1
    elif event == 'MOVIE':
        total_coffes += 2


if total_coffes > 5:
    print('You need extra sleep')
else:
    print(total_coffes)
