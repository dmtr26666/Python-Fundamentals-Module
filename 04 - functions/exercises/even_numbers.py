numbers_as_string = input().split()
numbers_as_int = list(map(int, numbers_as_string))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers_as_int))

print(even_numbers)