quatity_of_decorations_per_shopping = int(input())
days_till_christmas = int(input())

total_spirit = 0
if days_till_christmas % 10 == 0:
    total_spirit -= 30
total_cost = 0

for day_counter in range(1, days_till_christmas + 1):
    THIRD_DAY = False

    if day_counter % 11 == 0:
        quatity_of_decorations_per_shopping += 2

    if day_counter % 2 == 0:
        total_cost += 2 * quatity_of_decorations_per_shopping
        total_spirit += 5
    if day_counter % 3 == 0:
        total_cost += 8 * quatity_of_decorations_per_shopping
        total_spirit += 13
        THIRD_DAY = True
    if day_counter % 5 == 0:
        if THIRD_DAY:
            total_cost += 15 * quatity_of_decorations_per_shopping
            total_spirit += 47
        else:
            total_cost += 15 * quatity_of_decorations_per_shopping
            total_spirit += 17

    if day_counter % 10 == 0:
        total_spirit -= 20
        total_cost += 23

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")