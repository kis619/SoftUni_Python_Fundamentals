concealed_message = input()

command = input()
while not command == "Reveal":
    instructions = command.split(":|:")
    action = instructions[0]

    if action == "InsertSpace":
        index = int(instructions[1])
        left_half = concealed_message[:index]
        right_half = concealed_message[index:]
        concealed_message = left_half + " " + right_half

    elif action == "Reverse":
        substring = instructions[1]
        if substring not in concealed_message:
            print("error")
            command = input()
            continue
        else:
            concealed_message = concealed_message.replace(substring, "", 1)
            substring = substring[::-1]
            concealed_message += substring
    elif action == "ChangeAll":
        substring, replacement = instructions[1], instructions[2]
        concealed_message = concealed_message.replace(substring, replacement)

    print(concealed_message)

    command = input()

print(f"You have a new text message: {concealed_message}")
