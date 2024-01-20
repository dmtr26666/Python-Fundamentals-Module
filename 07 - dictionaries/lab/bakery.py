ingredients = input().split()

dictionary = {}

for i in range(0, len(ingredients), 2):
    key = ingredients[i]
    value = int(ingredients[i + 1])
    dictionary[key] = value

print(dictionary)
