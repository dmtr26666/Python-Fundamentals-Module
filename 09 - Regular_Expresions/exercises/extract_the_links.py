import re

pattern = r"((www)\.([A-Za-z0-9\-]+)\.([a-z]{1,}[a-z\.]*))\b"

text = input()

while text:

    matches = re.search(pattern, text)
    if matches:
        print(matches[0])

    text = input()

