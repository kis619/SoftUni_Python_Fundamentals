def replace_char_at_index(org_str, index, replacement):
    """Replace character at index in string org_str with the
    given replacement character."""
    new_str = org_str
    if index < len(org_str):
        new_str = org_str[0:index] + replacement + org_str[index + 1:]
    return new_str


blah = input()

position = 0
strength = 0
while position < len(blah) - 1:

    if blah[position] == ">":

        strength += int(blah[position + 1])
        if not int(blah[position + 1]) == 0:
            blah = replace_char_at_index(blah, position + 1, "")
            strength -= 1

    else:
        if not strength == 0:
            blah = replace_char_at_index(blah, position, "")
            strength -= 1
            position -= 1

    position += 1
print(blah)
