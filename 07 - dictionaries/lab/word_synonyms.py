words_count = int(input())

synonyms = {}

for _ in range(words_count):
    word = input()
    synonym = input()
    if word in synonyms.keys():
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]

for k, v in synonyms.items():
    print(f"{k} - {', '.join(v)}")