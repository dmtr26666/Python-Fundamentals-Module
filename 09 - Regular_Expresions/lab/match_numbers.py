import re

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

text = input()

mtaches = re.finditer(pattern, text)

for match in mtaches:
    print(match.group(), end=' ')