ingredients = {}

while True:
    command = input()

    if ':' not in command:
        break

    key, value = command.split(': ')

    if key in ingredients.keys():
        ingredients[key] += int(value)
    else:
        ingredients[key] = int(value)

print("Products in stock:")
for k, v in ingredients.items():
    print(f"- {k}: {v}")
print(f"Total Products: {len(ingredients.items())}")
print(f"Total Quantity: {sum(ingredients.values())}")