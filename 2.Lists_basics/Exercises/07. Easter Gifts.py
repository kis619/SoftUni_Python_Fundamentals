list_of_gifts = input().split()

action = input()
while not action == "No Money":
    command = action.split()
    label = command[0]
    item = command[1]
    if len(command) > 2:
        index = int(command[2])
    if "OutOfStock" in command:
        for the_item in range(len(list_of_gifts)):
            if list_of_gifts[the_item] == item:
                list_of_gifts[the_item] = None
    elif "Required" in command:
        if 0 < index < len(list_of_gifts):
            list_of_gifts[index] = item
    elif "JustInCase" in command:
        list_of_gifts[len(list_of_gifts) - 1] = item
    action = input()

new_list = []
for i in range(len(list_of_gifts)):
    if not list_of_gifts[i] == None:
        new_list.append(list_of_gifts[i])
print(" ".join(new_list))
