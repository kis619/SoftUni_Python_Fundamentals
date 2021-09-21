def checking_index(my_list, my_index):
    if my_index in range(len(my_list)) and not my_list[my_index] == -1:
        return True
    else:
        return False


def reduce_and_increase(my_list, my_index):
    target = my_list[my_index]
    new_list = []
    for number in my_list:
        if number == -1:
            new_list.append(number)
        elif number > target:
            number -= target
            new_list.append(number)
        else:
            number += target
            new_list.append(number)
    return new_list


targets = list(map(int, input().split()))
command = input()
shot_targets = 0
while not command == "End":
    index = int(command)
    if checking_index(targets, index):
        targets = reduce_and_increase(targets, index)
        targets[index] = -1
        shot_targets += 1
    command = input()

targets = [str(el) for el in targets]
print(f"Shot targets: {shot_targets} -> {' '.join(targets)}")