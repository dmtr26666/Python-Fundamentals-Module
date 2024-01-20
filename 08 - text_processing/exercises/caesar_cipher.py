clear_text = input()

coded_text = []

for letter in clear_text:
    letter_code = ord(letter)
    coded_text.append(chr(letter_code + 3))

print(f"{''.join(coded_text)}")