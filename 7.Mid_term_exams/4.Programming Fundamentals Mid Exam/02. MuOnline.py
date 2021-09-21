def potion(value, current_health):
    value = int(value)
    current_health += value
    if current_health > 100:
        value = value - (current_health - 100)
        current_health = 100

    print(f"You healed for {value} hp.")
    print(f"Current health: {current_health} hp.")
    return current_health


def chest(number_bitcoins, current_bitcoins):
    number_bitcoins = int(number_bitcoins)
    current_bitcoins += number_bitcoins
    print(f"You found {number_bitcoins} bitcoins.")
    return current_bitcoins


def monster(room, monster, damage, current_health):
    current_health -= int(damage)
    global alive
    if current_health > 0:
        print(f"You slayed {monster}.")
    else:
        print(f"You died! Killed by {monster}.")
        print(f"Best room: {room + 1}")
        alive = False

    return current_health


health = 100
bitcoins = 0
dungeon_rooms = input().split("|")

alive = True
for room_number in range(0, len(dungeon_rooms)):
    command, number = dungeon_rooms[room_number].split()
    if command == "potion":
        health = potion(number, health)
    elif command == "chest":
        bitcoins = chest(number, bitcoins)
    else:
        health = monster(room_number, command, number, health)
        if not alive:
            break

if alive:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
