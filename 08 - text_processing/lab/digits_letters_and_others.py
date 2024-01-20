text = input()

numbers = []
letters = []
chars = []

for letter in text:
    if letter.isdigit():
        numbers.append(letter)
    elif letter.isalpha():
        letters.append(letter)
    else:
        chars.append(letter)

print(f"{''.join(numbers)}\n{''.join(letters)}\n{''.join(chars)}")