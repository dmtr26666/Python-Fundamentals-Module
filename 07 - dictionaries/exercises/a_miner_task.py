resources = {}

while True:
    resource_type = input()
    if resource_type == 'stop':
        break
    amount = int(input())

    if resource_type in resources.keys():
        resources[resource_type] += amount
    else:
        resources[resource_type] = amount

for k, v in resources.items():
    print(f"{k} -> {v}")