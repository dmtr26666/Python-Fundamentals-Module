electrons = int(input())

filled_shells = []

counter = 1

while electrons > 0:
    value = 2*(counter**2)
    if value > electrons:
        filled_shells.append(electrons)
    else:
        filled_shells.append(value)

    electrons -= value
    counter += 1

print(filled_shells)