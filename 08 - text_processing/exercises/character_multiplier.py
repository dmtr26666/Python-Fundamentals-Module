str1, str2 = input().split()

iterations = len(str1) if len(str1) > len(str2) else len(str2)

total_sum = 0

for i in range(iterations):
    if i <= len(str1) - 1 and i <= len(str2) - 1:
        total_sum += ord(str1[i]) * ord(str2[i])
    elif i > len(str1) - 1:
        total_sum += ord(str2[i])
    else:
        total_sum += ord(str1[i])

print(total_sum)

