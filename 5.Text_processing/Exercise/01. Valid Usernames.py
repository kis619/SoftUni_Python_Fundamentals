def check_length(name):
    if 2 < len(name) < 17:
        return True
    return False


def check_chars(name):
    for character in name:
        if character.isalnum() or character == "-" or character == "_":
            continue
        else: return False
    return True


def check_for_blank_spaces(name):
    if " " in name:
        return False
    return True


usernames = input().split(", ")
valid = True
for username in usernames:
    if check_length(username) and check_chars(username) and check_for_blank_spaces(username):
        print(username)
    else:
        continue




