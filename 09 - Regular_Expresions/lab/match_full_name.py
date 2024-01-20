import re

text = input()
pattern = '\\b[A-Z][a-z]+ [A-Z][a-z]+\\b'

x = re.findall(pattern, text)

print(*x)
