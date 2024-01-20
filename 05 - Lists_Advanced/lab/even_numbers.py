numbers = [int(i) for i in input().split(', ')]

indices = []

for number in range(len(numbers)):
    if numbers[number] % 2 == 0:
        indices.append(number)

print(indices)
