def urgent(my_list, given_command):
    useless, item = given_command.split()
    if item not in my_list:
        my_list.insert(0, item)
    return my_list


def unnecessary(my_list, given_command):
    useless, item = given_command.split()
    if item in my_list:
        my_list.remove(item)
    return my_list


def correct(my_list, given_command):
    useless, old_item, new_item = given_command.split()
    if old_item in my_list:
        index = my_list.index(old_item)
        my_list[index] = new_item
    return my_list


def rearrange(my_list, given_command):
    useless, item = given_command.split()
    if item in my_list:
        my_list.remove(item)
        my_list.append(item)
    return my_list


shopping_list = input().split("!")
command = input()

while not command == "Go Shopping!":
    if "Urgent" in command:
        urgent(shopping_list, command)
    if "Unnecessary" in command:
        unnecessary(shopping_list, command)
    if "Correct" in command:
        correct(shopping_list, command)
    if "Rearrange" in command:
        rearrange(shopping_list, command)
    command = input()

print(", ".join(shopping_list))