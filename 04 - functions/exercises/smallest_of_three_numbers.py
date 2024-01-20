def smallest_num():
    return min(numbers_input)

numbers_input = [int(input()) for _ in range(3)]

result = smallest_num()
print(result)
