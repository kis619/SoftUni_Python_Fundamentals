# def take_odd(word):
#     new_string = ""
#     for i in range(len(word)):
#         if i % 2 == 1:
#             new_string += word[i]
#     print(new_string)
#
#     return new_string


# def cut(command_details, word):
#     useless, starting_index, substring_length = command_details.split()
#     starting_index, substring_length = int(starting_index), int(substring_length)
#     ending_index = starting_index + 3
#     substring = word[starting_index: ending_index]
#     word = word.replace(substring, "", 1)
#     print(word)
#
#     return word


# def substitute(command_details, word):
#     useless, substring, substitute_string = command_details.split()
#     if substring in word:
#         word = word.replace(substring, substitute_string)
#         print(word)
#     else:
#         print("Nothing to replace!")
#
#     return word


given_string = input()

command = input()
while not command == "Done":
    command_info = command.split()
    action = command_info[0]

    if action == "TakeOdd":

        new_string = ""
        for i in range(len(given_string)):
            if i % 2 == 1:
                new_string += given_string[i]

        given_string = new_string
        print(given_string)

    elif action == "Cut":
        starting_index = int(command_info[1])
        substring_length = int(command_info[2])
        starting_index, substring_length = int(starting_index), int(substring_length)
        ending_index = starting_index + 3
        substring = given_string[starting_index: ending_index]
        given_string = given_string.replace(substring, "", 1)
        print(given_string)

    elif action == "Substitute":
        substring = command_info[1]
        substitute_string = command_info[2]
        if substring in given_string:
            given_string = given_string.replace(substring, substitute_string)
            print(given_string)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {given_string}")
