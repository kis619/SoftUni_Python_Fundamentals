team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]

list_of_red_cards = input().split()
counter = 0

for each_element in list_of_red_cards:
    if each_element in team_a:
        team_a.remove(each_element)
    elif each_element in team_b:
        team_b.remove(each_element)
    counter += 1
    if len(team_a) < 7 or len(team_b) < 7:
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if len(team_a) < 7  or len(team_b) < 7:
    print("Game was terminated")