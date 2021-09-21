def valid_index(my_list, given_index):
    if given_index in range(len(my_list)):
        return True
    else:
        return False


def shoot(my_list, given_index, power):
    if valid_index(my_list, int(given_index)):
        my_list[int(given_index)] -= int(power)
        if my_list[int(given_index)] <= 0:
            my_list.remove(my_list[int(given_index)])

    return my_list


def add(my_list, given_index, given_value):
    if valid_index(my_list, int(given_index)):
        my_list.insert(int(given_index), int(given_value))

    else:
        print("Invalid placement!")

    return my_list


def strike(my_list, given_index, radius):
    left_index = int(given_index) - int(radius)
    right_index = int(given_index) + int(radius)
    if valid_index(my_list, left_index) and valid_index(my_list, right_index):
        del my_list[left_index:right_index + 1]

    else:
        print("Strike missed!")

    return my_list

targets = list(map(int, input().split()))

command = input()

while not command == "End":
    action, index, value = command.split()
    if action == "Shoot":
        targets = shoot(targets, index, value)
    elif action == "Add":
        targets = add(targets, index, value)
    elif action == "Strike":
        targets = strike(targets, index, value)
    command = input()

targets = [str(el) for el in targets]
print("|".join(targets))
