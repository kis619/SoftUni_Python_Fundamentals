energy = int(input())
command = input()
wins = 0
alive = True
while not command == "End of battle":
    distance = int(command)
    attempt = energy - distance
    if attempt >= 0:
        energy -= distance
        wins += 1
    else:
        alive = False
        break
    if wins % 3 == 0:
        energy += wins
    command = input()


if alive:
    print(f"Won battles: {wins}. Energy left: {energy}" )
else:
    print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")

