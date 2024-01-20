text = input()
final_text = ''
explosion_stength = 0

for index in range(len(text)):
    if explosion_stength > 0 and text[index] != '>':
        explosion_stength -= 1
    elif text[index] == '>':
        final_text += text[index]
        explosion_stength += int(text[index + 1])
    else:
        final_text += text[index]

print(final_text)




