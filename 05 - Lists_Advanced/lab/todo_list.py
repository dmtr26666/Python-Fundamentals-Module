notes = []

while True:
    command = input()

    if command == 'End':
        break
    else:
        notes.append(command)

notes_prioritezed = sorted(notes, key=lambda x: int(x.split('-')[0]))

clear_notes = [note.split('-')[1] for note in notes_prioritezed]

print(clear_notes)