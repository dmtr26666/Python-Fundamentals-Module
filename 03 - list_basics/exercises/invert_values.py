raw_string = input()

numbers = [int(n) for n in raw_string.split()]
inverted_numbers = []

for number in numbers:
    if number == 0:
        inverted_numbers.append(number)
    elif number < 0:
        inverted_numbers.append(abs(number))
    elif number > 0:
        inverted_numbers.append(-number)

print(inverted_numbers)


