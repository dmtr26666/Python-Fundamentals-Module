fire_stats = input().split('#')
amount_of_water = int(input())

cells_put_out = []
effort = 0
total_fire = 0

while amount_of_water > 0:

    for fire in range(len(fire_stats)):
        current_fire = fire_stats[fire].split(' = ')
        cell_value = int(current_fire[1])

        if (cell_value <= amount_of_water) and ((current_fire[0] == 'High' and 81 <= cell_value <= 125) or
                                                (current_fire[0] == 'Medium' and 51 <= cell_value <= 80) or
                                                (current_fire[0] == 'Low' and 1 <= cell_value <= 50)):
            amount_of_water -= cell_value
            effort += cell_value * 0.25
            total_fire += cell_value
            cells_put_out.append(cell_value)
        else:
            continue

    break

print("Cells:")
for cell in cells_put_out:
    print(f'- {cell}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')


