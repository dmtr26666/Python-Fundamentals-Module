money = input().split(', ')
money_as_numbers = []
for element in money:
    money_as_numbers.append(int(element))
number_of_beggars = int(input())

final_sums = []
index = 0

while index < number_of_beggars:
    sum_for_current_beggar = 0
    for i in range(index, len(money_as_numbers), number_of_beggars):
        sum_for_current_beggar += money_as_numbers[i]

    final_sums.append(sum_for_current_beggar)
    index += 1

print(final_sums)
