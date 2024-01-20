from sys import maxsize
divisor = int(input())
limit = int(input())

max_num = -maxsize

for i in range(1, limit + 1):
    if i % divisor == 0:
        if i > max_num:
            max_num = i

print(max_num)