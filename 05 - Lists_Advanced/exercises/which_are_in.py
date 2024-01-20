words1 = input().split(', ')
words2 = input().split(', ')

substrings = []

for word in words1:
    for word1 in words2:
        if word in word1:
            if word not in substrings:
                substrings.append(word)

print(substrings)