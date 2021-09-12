import sys


def exchange(a_list, a_index):
    """splits the list after the given index and exchanges the places of the two resulting sub-lists"""
    left_list = a_list[:a_index + 1]
    right_list = a_list[a_index + 1:]
    return right_list + left_list


def max_even(a_list):
    """returns the INDEX of the max even element"""
    max_num = -sys.maxsize
    needed_index = -1
    for i in range(len(a_list)):
        if a_list[i] % 2 == 0 and a_list[i] >= max_num:
            max_num = a_list[i]
            needed_index = i
    if needed_index == -1:
        return "No matches"
    else:
        return needed_index


def max_odd(a_list):
    """returns the INDEX of the max odd element"""
    max_num = -sys.maxsize
    needed_index = -1
    for i in range(len(a_list)):
        if not a_list[i] % 2 == 0 and a_list[i] >= max_num:
            max_num = a_list[i]
            needed_index = i
    if needed_index == -1:
        return "No matches"
    else:
        return needed_index


def min_even(a_list):
    min_num = sys.maxsize
    needed_index = -1
    for i in range(len(a_list)):
        if a_list[i] % 2 == 0 and a_list[i] <= min_num:
            min_num = a_list[i]
            needed_index = i
    if needed_index == -1:
        return "No matches"
    else:
        return needed_index


def min_odd(a_list):
    min_num = sys.maxsize
    needed_index = -1
    for i in range(len(a_list)):
        if not a_list[i] % 2 == 0 and a_list[i] <= min_num:
            min_num = a_list[i]
            needed_index = i
    if needed_index == -1:
        return "No matches"
    else:
        return needed_index


def first_thismany_even(a_list, given_count):
    even_nums = [even for even in a_list if even % 2 == 0]
    return even_nums[:given_count]


def first_thismany_odd(a_list, given_count):
    odd_nums = [odd for odd in a_list if not odd % 2 == 0]
    return odd_nums[:given_count]


def last_thismany_even(a_list, given_count):
    even_nums = [even for even in a_list if even % 2 == 0]
    return even_nums[-given_count:]


def last_thismany_odd(a_list, given_count):
    odd_nums = [odd for odd in a_list if not odd % 2 == 0]
    return odd_nums[-given_count:]


list_integers = [int(string) for string in input().split()]
command = input()

while not command == "end":
    action = command.split()
    if "exchange" in command:
        index = int(action[1])
        if index not in range(len(list_integers)):
            print("Invalid index")
        else:
            list_integers = exchange(list_integers, index)
    elif "max" in command:
        if action[1] == "even":
            print(max_even(list_integers))
        else:
            print(max_odd(list_integers))
    elif "min" in command:
        if action[1] == "even":
            print(min_even(list_integers))
        else:
            print(min_odd(list_integers))
    elif "first" in command:
        count = int(action[1])
        if count > len(list_integers):
            print("Invalid count")
        else:
            if action[2] == "even":
                print(first_thismany_even(list_integers, count))
            else:
                print(first_thismany_odd(list_integers, count))
    elif "last" in command:
        count = int(action[1])
        if count > len(list_integers):
            print("Invalid count")
        else:
            if action[2] == "even":
                print(last_thismany_even(list_integers, count))
            else:
                print(last_thismany_odd(list_integers, count))
    command = input()

print(list_integers)


