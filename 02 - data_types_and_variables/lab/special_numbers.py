n = int(input())

for i in range(1,n + 1):
    sum = 0
    special = False
    string = str(i)
    for y in range(len(string)):
        digit = string[y]
        sum += int(digit)

    if sum == 5 or sum == 7 or sum == 11:
        special = True

    print(f'{i} -> {special}')

