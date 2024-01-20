import re

text = input()
word = input()
pattern = fr"\b{word}\b"


matches = re.findall(pattern, text, re.I)

print(len(matches))

