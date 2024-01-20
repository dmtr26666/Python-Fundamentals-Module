
friends = input().split(', ')
command = input()

while command != 'Report':
    command = command.split()
    operation = command[0]

    if operation == 'Blacklist':
        name = command[1]
        if name in friends:
            friends[friends.index(name)] = 'Blacklisted'
            print(f'{name} was blacklisted.')
        else:
            print(f'{name} was not found.')
    elif operation == 'Error':
        index = int(command[1])
        if len(friends) - 1 >= index >= 0:
            name = friends[index]
            if name != 'Blacklisted' and name != 'Lost':
                friends[index] = 'Lost'
                print(f'{name} was lost due to an error.')
    elif operation == 'Change':
        index = int(command[1])
        if len(friends) - 1 >= index >= 0:
            old_name = friends[index]
            new_name = command[2]
            friends[index] = new_name
            print(f'{old_name} changed his username to {new_name}.')

    command = input()
else:
    blacklisted_count = friends.count('Blacklisted')
    lost_count = friends.count('Lost')
    print(f"Blacklisted names: {blacklisted_count}")
    print(f"Lost names: {lost_count}")
    print(f"{' '.join(friends)}")