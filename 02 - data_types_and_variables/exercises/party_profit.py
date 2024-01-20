group_size = int(input())
trip_length = int(input())

total_coins = 0

for day_counter in range(1, trip_length + 1):
    total_coins += 50

    if day_counter % 10 == 0:
        group_size -= 2
    if day_counter % 15 == 0:
        group_size += 5

    total_coins -= 2 * group_size

    if day_counter % 3 == 0:
        total_coins -= 3 * group_size
    if day_counter % 5 == 0:
        total_coins += 20 * group_size
        if day_counter % 3 == 0:
            total_coins -= 2 * group_size

print(f"{group_size} companions received {int(total_coins / group_size)} coins each.")
