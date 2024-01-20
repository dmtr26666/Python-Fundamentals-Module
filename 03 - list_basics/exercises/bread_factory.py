day_events = input().split('|')

energy = 100
coins = 100
BANKRUPT = False

for event in day_events:
    current_event = event.split('-')
    number = int(current_event[1])

    if current_event[0] == 'rest':
        energy_gained = 0
        if energy == 100:
            print(f"You gained {energy_gained} energy.")
            print(f"Current energy: {energy}.")
            continue
        elif number <= 100 - energy:
            energy_gained = number
            energy += energy_gained
            print(f'You gained {energy_gained} energy.')
            print(f"Current energy: {energy}.")
        elif number > 100 - energy:
            energy_gained = 100 - energy
            energy += energy_gained
            print(f'You gained {energy_gained} energy.')
            print(f"Current energy: {energy}.")

    elif current_event[0] == 'order':
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
            continue
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {current_event[0]}.")
        else:
            print(f"Closed! Cannot afford {current_event[0]}.")
            BANKRUPT = True
            break


if not BANKRUPT:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
