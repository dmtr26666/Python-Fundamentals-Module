text = input().split()
alphabet = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

total_sum = 0

for part in text:
    number = int(part[1:-1])

    if part[0].isupper():
        number = number / alphabet.index(part[0].upper())
    else:
        number = number * alphabet.index(part[0].upper())

    if part[-1].isupper():
        number = number - alphabet.index(part[-1].upper())
    else:
        number = number + alphabet.index(part[-1].upper())

    total_sum += number

print(f"{total_sum:.2f}")