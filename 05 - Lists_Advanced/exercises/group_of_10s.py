from math import ceil


def roundup(x):
    return ceil(x / 10.0) * 10

def find_nums(list, max_num):
    nums = []
    min_num = max_num - 10
    for num in list:
        if min_num < num <= max_num:
            nums.append(num)

    return nums

numbers_list = [int(num) for num in input().split(', ')]

max_num = roundup(max(numbers_list))

for group in range(10, max_num + 10, 10):
    print(f"Group of {group}'s: {find_nums(numbers_list, group)}")