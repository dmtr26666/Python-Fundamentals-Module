deck = input().split()
shuffles_count = int(input())

counter = 0

while counter < shuffles_count:
    deck_part1 = []
    deck_part2 = []
    current_shuffle = []

    for i in range(len(deck) // 2):
        deck_part1.append(deck[i])
        deck_part2.append(deck[i + len(deck) // 2])

    for y in range(len(deck) // 2):
        current_shuffle.append(deck_part1[y])
        current_shuffle.append(deck_part2[y])

    for x in range(len(current_shuffle) - 1):
        deck[x] = current_shuffle[x]

    counter += 1

print(deck)
