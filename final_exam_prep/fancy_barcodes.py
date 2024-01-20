import re

pattern = r"^@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+$"

barcode_count = int(input())

for _ in range(barcode_count):
    barcode = input()
    group = ''
    match = re.search(pattern, barcode)

    if match:
        for letter in match.group():
            if letter.isnumeric():
                group += str(letter)
    else:
        print("Invalid barcode")
        continue

    print(f"Product group: {'00' if group == '' else int(group)}")


