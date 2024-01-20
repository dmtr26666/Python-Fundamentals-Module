capacity = 255

lines = int(input())
litters_in_the_tank = 0

for i in range(lines):
    litters_poured = int(input())

    if litters_poured > capacity - litters_in_the_tank:
        print("Insufficient capacity!")
        continue
    else:
        litters_in_the_tank += litters_poured

print(litters_in_the_tank)
