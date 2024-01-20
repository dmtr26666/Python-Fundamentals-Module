def register(username, license_plate_number, registered_users):
    if username in registered_users.keys() and registered_users[username] is not None:
        print(f"ERROR: already registered with plate number {registered_users[username]}")
    else:
        registered_users[username] = license_plate_number
        print(f"{username} registered {license_plate_number} successfully")

    return registered_users


def unregister(username, registered_users):
    if username not in registered_users:
        print(f"ERROR: user {username} not found")
    else:
        registered_users.pop(username)
        print(f"{username} unregistered successfully")

    return registered_users


number_of_commands = int(input())

parking_users = {}

for _ in range(number_of_commands):
    command = input().split()

    if command[0] == 'unregister':
        operation = command[0]
        name = command[1]
    else:
        operation = command[0]
        name = command[1]
        plate_number = command[2]

    if operation == 'register':
        parking_users = register(name, plate_number, parking_users)
    else:
        parking_users = unregister(name, parking_users)


for name, license_plate in parking_users.items():
    print(f"{name} => {license_plate}")