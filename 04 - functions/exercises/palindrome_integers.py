numbers_as_string = [num for num in input().split(", ")]

for num in numbers_as_string:
    if num == num[::-1]:
        print("True")
    else:
        print("False")