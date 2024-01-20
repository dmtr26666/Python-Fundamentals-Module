text = input()

last_char = ''
final_text = ''

for char in text:
    if char != last_char:
        final_text += char
        last_char = char

print(final_text)
