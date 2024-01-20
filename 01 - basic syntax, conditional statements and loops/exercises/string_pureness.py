n = int(input())

for i in range(n):
    string = input()
    ALERT = False
    for y in range(len(string)):
        letter = string[y]
        if string[y] == "," or string[y] == "." or string[y] == "_":
            ALERT = True
            break

    if ALERT:
        print(f'{string} is not pure!')
    else:
        print(f'{string} is pure.')