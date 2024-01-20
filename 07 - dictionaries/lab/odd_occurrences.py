words_list = input().split()

new_dict = {}

for word in words_list:
    if word.lower() in new_dict.keys():
        new_dict[word.lower()] += 1
    else:
        new_dict[word.lower()] = 1

for k, v in new_dict.items():
    if v % 2 != 0:
        print(k, end=' ')
