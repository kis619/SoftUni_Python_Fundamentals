number_of_people = int(input())
days = int(input())
coins = 0
for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        number_of_people -= 2
    if current_day % 15 == 0:
        number_of_people+= 5
    coins += 50 - number_of_people * 2
    if current_day % 3 == 0:
        coins -= number_of_people * 3
    if current_day % 5 == 0:
        coins += number_of_people * 20
        if current_day % 3 == 0:
            coins -= number_of_people * 2
coins_per_person = coins / number_of_people
print(f"{number_of_people} companions received {int(coins_per_person)} coins each.")