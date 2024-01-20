factor = int(input())
count = int(input())

last_num_added_to_list = 0

numbers = []

for i in range(count):
    new_num = last_num_added_to_list + factor
    numbers.append(new_num)
    last_num_added_to_list = new_num

print(numbers)

