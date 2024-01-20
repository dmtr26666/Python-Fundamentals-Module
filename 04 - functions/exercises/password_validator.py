import string
alphabet = list(string.ascii_letters)
nums = list(string.digits)


def validator(password):
    rule1 = False
    rule2 = True
    rule3 = False

    digits_count = 0

    if 6 <= len(password) <= 10:
        rule1 = True

    for char in password:
        if char in nums:
            digits_count += 1
        if char not in alphabet and char not in nums:
            rule2 = False

    if digits_count >= 2:
        rule3 = True

    return rule1, rule2, rule3

result = validator(input())


if result[0] == True and result[1] == True and result[2] == True:
    print("Password is valid")
else:
    if result[0] == False:
        print("Password must be between 6 and 10 characters")
        print()
    if result[1] == False:
        print("Password must consist only of letters and digits")
        print()
    if result[2] == False:
        print("Password must have at least 2 digits")
        print()


