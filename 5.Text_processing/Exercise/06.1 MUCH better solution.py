given_string = input()

position = 0

while position < len(given_string) - 1:

    if given_string[position] == given_string[position + 1]:
        given_string = given_string.replace(f"{given_string[position]}{given_string[position + 1]}", given_string[position])

    else:
        position += 1

print(given_string)