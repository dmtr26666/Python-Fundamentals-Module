import re

pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"

total_spend = 0
items = []

text = input()
while text != 'Purchase':

    matches = re.search(pattern, text)
    if matches:
        items.append(matches.group(1))
        total_spend += (float(matches.group(2)) * int(matches.group(3)))

    text = input()

print("Bought furniture:")
for item in items:
    print(item)
print(f"Total money spend: {total_spend:.2f}")

