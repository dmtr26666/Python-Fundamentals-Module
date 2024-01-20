

employees_happiness = [int(value) for value in input().split()]
factor = int(input())

multiplied_happiness = list(map(lambda x: x * factor, employees_happiness))
average_happiness = sum(multiplied_happiness) / len(multiplied_happiness)
happy_employees = 0

for happiness in multiplied_happiness:
    if happiness >= average_happiness:
        happy_employees += 1

if happy_employees >= len(multiplied_happiness) / 2:
    print(f"Score: {happy_employees}/{len(multiplied_happiness)}. Employees are happy!")
else:
    print(f"Score: {happy_employees}/{len(multiplied_happiness)}. Employees are not happy!")