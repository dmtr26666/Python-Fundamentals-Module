ingredients = input().split()

dictionary = {}

for i in range(0, len(ingredients), 2):
    key = ingredients[i]
    value = int(ingredients[i + 1])
    dictionary[key] = value

searched_elements = input().split()

for element in searched_elements:
    if element in dictionary.keys():
        print(f"We have {dictionary[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")