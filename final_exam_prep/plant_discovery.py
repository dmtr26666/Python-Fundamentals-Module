plants_count = int(input())

plant_and_rarity = {}

for _ in range(plants_count):
    plant, rarity = input().split('<->')
    if plant not in plant_and_rarity.keys():
        plant_and_rarity[plant] = {"rarity": int(rarity), "rating": []}
    else:
        plant_and_rarity[plant]["rarity"] = int(rarity)


while True:
    command = input()
    if command == 'Exhibition':
        break

    action = command.split(': ')[0]

    if action == "Rate":
        plant, rating = command.split(': ')[1].split(" - ")
        if plant in plant_and_rarity.keys():
            plant_and_rarity[plant]["rating"].append(int(rating))
        else:
            print('error')
    elif action == "Update":
        plant, new_rarity = command.split(': ')[1].split(' - ')
        if plant in plant_and_rarity.keys():
            plant_and_rarity[plant]["rarity"] = int(new_rarity)
        else:
            print('error')
    elif action == "Reset":
        plant = command.split(': ')[1]
        if plant in plant_and_rarity.keys():
            plant_and_rarity[plant]["rating"].clear()
        else:
            print("error")

print("Plants for the exhibition: ")
for plant_name in plant_and_rarity.keys():
    if plant_and_rarity[plant_name]["rating"]:
        average_rating = sum(plant_and_rarity[plant_name]["rating"]) / len(plant_and_rarity[plant_name]["rating"])
    else:
        average_rating = 0
    print(f"- {plant_name}; Rarity: {plant_and_rarity[plant_name]['rarity']}; Rating: {average_rating:.2f}")
