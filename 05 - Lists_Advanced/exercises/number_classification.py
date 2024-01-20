numbers_list = [int(number) for number in input().split(', ')]

pos_list = [num for num in numbers_list if num >= 0]
neg_list = [num for num in numbers_list if num < 0]
even_list = [num for num in numbers_list if num % 2 == 0]
odd_list =[num for num in numbers_list if num % 2 != 0]

print(f"Positive: {', '.join([str(name) for name in pos_list])}\
       \nNegative: {', '.join([str(name) for name in neg_list])} \
       \nEven: {', '.join([str(name)  for name in even_list])}\
       \nOdd: {', '.join([str(name) for name in odd_list])}")

