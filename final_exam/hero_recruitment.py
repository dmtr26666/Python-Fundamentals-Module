

command = input()

heroes = {}

while command != 'End':
    action = command.split()[0]

    if action == 'Enroll':
        hero_name = command.split()[1]
        if hero_name not in heroes.keys():
            heroes[hero_name] = {'spells': []}
        else:
            print(f"{hero_name} is already enrolled.")
    elif action == 'Learn':
        hero_name = command.split()[1]
        spell_name = command.split()[2]

        if hero_name in heroes.keys() and spell_name not in heroes[hero_name]['spells']:
            heroes[hero_name]['spells'].append(spell_name)
        elif hero_name not in heroes.keys():
            print(f"{hero_name} doesn't exist.")
        elif spell_name in heroes[hero_name]['spells']:
            print(f"{hero_name} has already learnt {spell_name}.")
    elif action == 'Unlearn':
        hero_name = command.split()[1]
        spell_name = command.split()[2]

        if hero_name in heroes.keys() and spell_name in heroes[hero_name]['spells']:
            heroes[hero_name]['spells'].remove(spell_name)
        elif hero_name not in heroes.keys():
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in heroes[hero_name]['spells']:
            print(f"{hero_name} doesn't know {spell_name}.")

    command = input()
else:
    print("Heroes:")
    for hero in heroes.items():
        print(f"== {hero[0]}: {', '.join(hero[1]['spells'])}")
