def swap(given_command, my_list):
    useless, index1, index2 = given_command.split()
    my_list[int(index1)], my_list[int(index2)] = my_list[int(index2)], my_list[int(index1)]
    return my_list


def multiply(given_command, my_list):
    useless, index1, index2 = given_command.split()
    index1 = int(index1)
    index2 = int(index2)
    my_list[index1] = my_list[index1] * my_list[index2]
    return my_list


def decrease(my_list):
    my_list = [el + (- 1) for el in my_list]
    # new_list = []
    # for el in my_list:
    #     element = el + (-1)
    #     new_list.append(element)
    # my_list = new_list
    return my_list


integers = [int(el) for el in input().split()]


command = input()
while not command == "end":
    if "swap" in command:
        swap(command, integers)
    elif "multiply" in command:
        multiply(command, integers)
    elif "decrease" in command:
        decrease(integers)
    command = input()

integers = [str(el) for el in integers]
print(f"{', '.join(integers)}")
