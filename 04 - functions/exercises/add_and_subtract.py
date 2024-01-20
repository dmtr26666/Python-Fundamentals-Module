def sum_numbers():
    sum_of_numbers = numbers_list[0] + numbers_list[1]
    return sum_of_numbers

def subtract():
    result = sum_numbers() - numbers_list[2]
    return result


numbers_list = [int(input()) for _ in range(3)]

print(subtract())


