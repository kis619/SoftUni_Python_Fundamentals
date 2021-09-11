team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

list_of_red_cards = input().split()
the_game_was_terminated = False

for card in list_of_red_cards:
    card_info = card.split("-")

    team_name = card_info[0]
    player_number = int(card_info[1])

    if team_name == "A" and player_number in team_a:
        team_a.remove(player_number)
    elif team_name == "B" and player_number in team_b:
        team_b.remove(player_number)
    if len(team_a) < 7 or len(team_b) < 7:
        the_game_was_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if the_game_was_terminated:
    print("Game was terminated")