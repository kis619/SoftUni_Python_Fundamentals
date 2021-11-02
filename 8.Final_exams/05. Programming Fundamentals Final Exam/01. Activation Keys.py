def contains(commands, key):
    command_taken, substring = commands.split(">>>")
    if substring in key:
        print(f"{key} contains {substring}")
    else:
        print("Substring not found!")


def flip(commands, key):
    command_taken, case, start_index, end_index = commands.split(">>>")
    left_part = key[:int(start_index)]
    substring = key[int(start_index):int(end_index)]
    right_part = key[int(end_index):]
    if case == "Upper":
        substring = substring.upper()
    else:
        substring = substring.lower()
    key = left_part + substring + right_part
    print(key)

    return key


def slicing(commands, key):
    command_taken, start_index, end_index = commands.split(">>>")
    start_index, end_index = int(start_index), int(end_index)
    left_part = key[:int(start_index)]
    right_part = key[int(end_index):]
    key = left_part + right_part
    print(key)

    return key


activation_key = input()

command = input()
while not command == "Generate":
    command_info = command.split(">>>")
    action = command_info[0]

    if action == "Contains":
        contains(command, activation_key)
    elif action == "Flip":
        activation_key = flip(command, activation_key)
    elif action == "Slice":
        activation_key = slicing(command, activation_key)
    command = input()

print(f"Your activation key is: {activation_key}")
