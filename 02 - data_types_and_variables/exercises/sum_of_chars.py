characters = int(input())

sum_of_chars = 0

for i in range(characters):
    char = input()
    current_num = ord(char)
    sum_of_chars += current_num

print(f"The sum equals: {sum_of_chars}")
