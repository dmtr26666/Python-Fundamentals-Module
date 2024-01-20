text = input()

emoticons = []

last_index = 0

for _ in range(text.count(':')):
    element_index = text.index(':', last_index)
    emoticons.append(text[element_index:element_index + 2])
    last_index = element_index + 1

print('\n'.join(emoticons))

