n = int(input())
special_word = input()

lst = []
filtered_list = []

for _ in range(n):
    string = input()
    lst.append(string)


for string in lst:
    if special_word in string:
        filtered_list.append(string)

print(lst)
print(filtered_list)