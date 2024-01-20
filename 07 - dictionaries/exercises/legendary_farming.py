items_dict = {'motes': 0, 'fragments': 0, 'shards': 0}
won = False

while True:
    items = input().split()
    for i in range(0, len(items), 2):
        material = items[i + 1].lower()
        quantity = int(items[i])

        if material in items_dict.keys():
            items_dict[material] += quantity
        else:
            items_dict[material] = quantity

        if "motes" in items_dict.keys() and items_dict["motes"] >= 250:
            print("Dragonwrath obtained!")
            items_dict['motes'] -= 250
            won = True
            break
        elif "fragments" in items_dict.keys() and items_dict["fragments"] >= 250:
            print("Valanyr obtained!")
            items_dict['fragments'] -= 250
            won = True
            break
        elif "shards" in items_dict.keys() and items_dict["shards"] >= 250:
            print("Shadowmourne obtained!")
            items_dict['shards'] -= 250
            won = True
            break
    if won:
        break

print(f"shards: {items_dict['shards']}")
print(f"fragments: {items_dict['fragments']}")
print(f"motes: {items_dict['motes']}")

items_dict.pop('shards')
items_dict.pop('fragments')
items_dict.pop('motes')

for k,v in items_dict.items():
    print(f"{k}: {v}")