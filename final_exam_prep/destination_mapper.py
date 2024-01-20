import re

pattern = r"=[A-Z][A-Za-z]{2,}=|\/[A-Z][A-Za-z]{2,}\/"

text = input()

matches = re.findall(pattern, text)

total_points = 0
for i in range(len(matches)):
    matches[i] = matches[i][1:len(matches[i]) - 1]
    total_points += len(matches[i])

print(f"Destinations: {', '.join(matches)}")
print(f"Travel Points: {total_points}")