houses = list(map(int, input().split("@")))

command = input()
position = 0
while "Love!" not in command:
    jump, length = command.split()
    length = int(length)
    position += length
    if position > len(houses) - 1:
        position = 0

    if houses[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        houses[position] -= 2
        if houses[position] == 0:
            print(f"Place {position} has Valentine's day." )
    command = input()

print(f"Cupid's last position was {position}.")
if sum(houses) == 0:
    print("Mission was successful.")
else:
    houses = [house for house in houses if house > 0]
    print(f"Cupid has failed {len(houses)} places.")