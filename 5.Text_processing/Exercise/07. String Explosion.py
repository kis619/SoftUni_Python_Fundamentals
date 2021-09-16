def replace_char_at_index(org_str, index, replacement):
    """Replace character at index in string org_str with the
    given replacement character."""
    new_str = org_str
    if index < len(org_str):
        new_str = org_str[0:index] + replacement + org_str[index + 1:]
    return new_str


def check_for_digits(given_word, current_position):
    number_as_string = 0
    for positionn in range(current_position + 1, len(given_word)):
        if given_word[positionn].isdigit():
            number_as_string += int(given_word[positionn])
        if not positionn == len(given_word) - 1:
            if given_word[positionn] == ">" or given_word[positionn + 1] == ">":
                break

    return int(number_as_string)


word = input()
force = 0
position = 0

while position < len(word):

    if word[position] == ">":
        new_force = check_for_digits(word, position)
        force += new_force
        if new_force > 0:
            for _ in range(len(str(new_force))):
                word = replace_char_at_index(word, position + 1, "")

            force -= len(str(new_force))

    else:
        if force > 0:
            word = replace_char_at_index(word, position, "")
            force -= 1
            position -= 1

    position += 1

print(word)






