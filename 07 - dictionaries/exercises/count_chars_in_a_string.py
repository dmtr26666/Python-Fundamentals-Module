word = input()

new_dict = {}

for letter in word:
    if letter == ' ':
        continue
    if letter in new_dict.keys():
        new_dict[letter] += 1
    else:
        new_dict[letter] = 1

for k, v in new_dict.items():
    print(f"{k} -> {v}")