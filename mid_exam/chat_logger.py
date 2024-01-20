chat = []

command = input()

while command != 'end':
    command = command.split()
    operation = command[0]

    if operation == 'Chat':
        chat.append(command[1])
    elif operation == 'Delete':
        message = command[1]
        if message in chat:
            chat.remove(message)
    elif operation == 'Edit':
        message = command[1]
        edited_message = command[2]
        if message in chat:
            chat[chat.index(message)] = edited_message
    elif operation == 'Pin':
        message = command[1]
        if message in chat:
            chat.remove(message)
            chat.append(message)
    elif operation == 'Spam':
        messages = command[1:]
        for mes in messages:
            chat.append(mes)

    command = input()
else:
    for chats in chat:
        print(chats)