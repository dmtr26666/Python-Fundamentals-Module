cards_string = input()

team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
GAME_TERMINATED = False
cards_list = cards_string.split()

for card in cards_list:
    if card[:1] == 'A':
        player_number = int(card[2:])
        if player_number not in team_A:
            continue
        else:
            team_A.remove(player_number)
    else:
        player_number = int(card[2:])
        if player_number not in team_B:
            continue
        else:
            team_B.remove(player_number)

    if len(team_A) < 7 or len(team_B) < 7:
        GAME_TERMINATED = True
        break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if GAME_TERMINATED:
    print('Game was terminated')
