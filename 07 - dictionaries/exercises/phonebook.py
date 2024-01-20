phonebook = {}

while True:
    command = input()
    if '-' not in command:
        count = int(command)
        break

    name, phone = command.split('-')

    phonebook[name] = phone

for _ in range(count):
    name = input()

    if name in phonebook.keys():
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")