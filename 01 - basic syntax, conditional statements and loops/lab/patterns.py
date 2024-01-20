max_cols = int(input())

for i in range(1, max_cols + 1):
    print('*' * i)
for y in range(max_cols - 1, 0, -1):
    print('*' * y)