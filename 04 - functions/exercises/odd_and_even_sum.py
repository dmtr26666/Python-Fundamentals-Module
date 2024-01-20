def odd_and_even_sum(number):
    odd_list = []
    even_list = []

    for num in number:
        num_as_int = int(num)

        if num_as_int % 2 == 0:
            even_list.append(num_as_int)
        else:
            odd_list.append(num_as_int)

    odd_sum = sum(odd_list)
    even_sum = sum(even_list)

    return odd_sum, even_sum

result = odd_and_even_sum(input())

print(f"Odd sum = {result[0]}, Even sum = {result[1]}")