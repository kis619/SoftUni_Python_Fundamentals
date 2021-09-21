def collect(my_list, current_item):
    if current_item not in my_list:
        my_list.append(current_item)
    return my_list


def drop(my_list, current_item):
    if current_item in my_list:
        my_list.remove(current_item)
    return my_list


def combine_items(my_list, current_items: str):
    old_item, new_item = current_items.split(":")
    if old_item in my_list:
        index = my_list.index(old_item)
        my_list.insert(index + 1, new_item)
    return my_list


def renew(my_list, current_item):
    if current_item in my_list:
        my_list.remove(current_item)
        my_list.append(current_item)
    return my_list


list_of_items = input().split(", ")
command = input()

while not command == "Craft!":
    action, item = command.split(" - ")
    if action == "Collect":
        list_of_items = collect(list_of_items, item)
    elif action == "Drop":
        list_of_items = drop(list_of_items, item)
    elif action == "Combine Items":
        list_of_items = combine_items(list_of_items, item)
    elif action == "Renew":
        list_of_items = renew(list_of_items, item)
    command = input()

print(", ".join(list_of_items))