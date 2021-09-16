message = input().upper()
temp_string = ""
final_message = ""

position = 0
while position < len(message):
    char = message[position]

    if not char.isdigit():
        temp_string += char

    else:
        if not position == len(message) - 1 and message[position + 1].isdigit():
            char = f"{char}{message[position + 1]}"
        final_message += temp_string * int(char)
        temp_string = ""

    position += 1

print(f"Unique symbols used: {len(set(final_message))}")
print(final_message)
