nums_list = [int(num) for num in input()]
reversed_list = sorted(nums_list, reverse=True)
print(''.join(map(str, reversed_list)))