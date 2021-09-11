gift_names = [gift for gift in input().split()]
commands_input = input()

while not commands_input == "No Money":
    command = commands_input.split()[0]
    gift = commands_input.split()[1]

    if command == "OutOfStock":
        for i in range(len(gift_names)):
            if gift[i] == "gift":
                gift[i] = "None"
    if command == "Required":
        index = int(commands_input.split()[2])
        if 0 <= index < len(gift_names):
            gift_names[index] = gift

    if command == "JustInCase":
        gift_names[-1] = gift

    commands_input = input()

no_none = [el for el in gift_names if not el == "None"]
print(" ".join(no_none))


