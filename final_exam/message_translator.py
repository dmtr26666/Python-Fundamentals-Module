import re

pattern = r"^!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]$"

strings_count = int(input())

for _ in range(strings_count):
    raw_command = input()

    match = re.search(pattern, raw_command)
    if match:
        message_as_ascii = []
        command = match.group(1)
        message = match.group(2)
        for letter in message:
            message_as_ascii.append(str(ord(letter)))
        print(f"{command}: {' '.join(message_as_ascii)}")
    else:
        print("The message is invalid")


