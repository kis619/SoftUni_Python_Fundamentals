def check_index(index, given_string):
    if index in range(len(given_string)):
        return True
    return False


def add(command, given_string):
    useless, index, place = command.split(":")
    index = int(index)

    if check_index(index, given_string):
        left_slice = given_string[:index]
        right_slice = given_string[index:]
        given_string = left_slice + place + right_slice
    return given_string


def remove(command, given_string):
    useless, start_index, end_index = command.split(":")
    start_index, end_index = int(start_index), int(end_index)

    if check_index(start_index, given_string) and check_index(end_index, given_string):
        left_slice = given_string[:start_index]
        right_slice = given_string[end_index + 1:]
        given_string = left_slice + right_slice
    return given_string


def switch(command, given_string):
    useless, old_string, new_string = command.split(":")

    if old_string in given_string:
        given_string = given_string.replace(old_string, new_string)

    return given_string


all_stops = input()
command = input()

while not command == "Travel":

    if "Add" in command:
        all_stops = add(command, all_stops)

    elif "Remove" in command:
        all_stops = remove(command, all_stops)

    elif "Switch" in command:
        all_stops = switch(command, all_stops)

    print(all_stops)
    command = input()

print(f"Ready for world tour! Planned stops: {all_stops}")