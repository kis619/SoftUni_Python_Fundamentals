list_of_events = input().split("|")
energy = 100
coins = 100
bankrupt = False
for each_event in list_of_events:
    event = each_event.split("-")
    event_or_ingredient = event[0]
    number = int(event[1])
    if event_or_ingredient == "rest":
        gained = number
        if energy + gained > 100:
            gained = 100 - energy

        energy += gained
        print(f"You gained {gained} energy.")
        print(f"Current energy: {energy}.")

    elif event_or_ingredient == "order":
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {event_or_ingredient}.")
        else:
            bankrupt = True
            print(f"Closed! Cannot afford {event_or_ingredient}.")
            break
if not bankrupt:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

