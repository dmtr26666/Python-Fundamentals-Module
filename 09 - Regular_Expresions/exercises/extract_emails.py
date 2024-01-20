import re

pattern = r"\s(([A-Za-z0-9]+[A-Za-z0-9\.\-_]*)@([A-Za-z\-]+)(\.[A-Za-z]+)+)\b"

text = input()

matches = re.findall(pattern, text)

for match in matches:
    print(match[0])