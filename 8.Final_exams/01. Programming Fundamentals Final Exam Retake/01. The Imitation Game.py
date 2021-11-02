def move(message, og_command):
    number = int(og_command.split("|")[1])
    left_part = message[:number]
    right_part = message[number:]
    message = right_part + left_part
    return message


def insert(message, og_command):
    given_index = int(og_command.split("|")[1])
    value = og_command.split("|")[2]
    left_part = message[:given_index]
    right_part = message[given_index:]
    message = left_part + value + right_part
    return message


def change_all(message, og_command):
    substring = og_command.split("|")[1]
    replacement = og_command.split("|")[2]
    message = message.replace(substring, replacement)
    return message


encrypted_message = input()

command = input()
while not command == "Decode":

    operation = command.split("|")[0]
    if operation == "Move":
        encrypted_message = move(encrypted_message, command)
    elif operation == "Insert":
        encrypted_message = insert(encrypted_message, command)
    elif operation == "ChangeAll":
        encrypted_message = change_all(encrypted_message, command)

    command = input()

print(f"The decrypted message is: {encrypted_message}")
