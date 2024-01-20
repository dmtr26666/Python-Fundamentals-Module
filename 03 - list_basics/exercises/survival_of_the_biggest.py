numbers_string = input().split()
remover = int(input())

numbers_integer = []
sorted_numbers = []
for element in numbers_string:
    numbers_integer.append(int(element))
    sorted_numbers.append(int(element))
sorted_numbers.sort()

for i in range(remover):
    number = sorted_numbers[i]
    numbers_integer.remove(number)

for y in range(len(numbers_integer)):
    if y == len(numbers_integer) - 1:
        print(numbers_integer[y])
    else:
        print(numbers_integer[y], end=', ')
