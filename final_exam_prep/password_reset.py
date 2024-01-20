def take_odd(password):
    new_password = ''
    for i in range(1, len(password), 2):
        new_password += password[i]

    return new_password

def cut(index, length, password:str):
    substring = password[index:index + length]
    new_password = password.replace(substring, '', 1)

    return new_password


def substitude(substring, substitude_string, password):
    new_password = password
    if substring in password:
        new_password = password.replace(substring, substitude_string)

    return new_password


password = input()

command = input()

while command != 'Done':
    action = command.split()[0]

    if action == 'TakeOdd':
        password = take_odd(password)
        print(password)
    elif action == 'Cut':
        _, index, length = command.split()
        password = cut(int(index), int(length), password)
        print(password)
    elif action == 'Substitute':
        _, substring, substitude_string = command.split()
        old_password = password
        password = substitude(substring, substitude_string, password)
        if password == old_password:
            print('Nothing to replace!')
        else:
            print(password)

    command = input()

print(f"Your password is: {password}")