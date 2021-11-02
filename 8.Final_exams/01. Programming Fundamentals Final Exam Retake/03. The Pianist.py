def add(og_command):
    useless, piece_name, composer_name, key_of_piece = og_command.split("|")
    if piece_name in pieces_and_info:
        print(f"{piece_name} is already in the collection!")
    else:
        print(f"{piece_name} by {composer_name} in {key_of_piece} added to the collection!")
        pieces_and_info[piece_name] = [composer_name, key_of_piece]

    return pieces_and_info


def remove(og_command):
    piece_name = og_command.split("|")[1]
    if piece_name not in pieces_and_info:
        print(f"Invalid operation! {piece_name} does not exist in the collection.")
    else:
        del pieces_and_info[piece_name]
        print(f"Successfully removed {piece_name}!")

    return pieces_and_info


def change_key(og_command):
    useless, piece_name, new_key = og_command.split("|")
    if piece_name not in pieces_and_info:
        print(f"Invalid operation! {piece_name} does not exist in the collection.")
    else:
        pieces_and_info[piece_name][1] = new_key
        print(f"Changed the key of {piece_name} to {new_key}!")

    return pieces_and_info


number_of_pieces = int(input())

pieces_and_info = {}
for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    pieces_and_info[piece] = [composer, key]

command = input()
while not command == "Stop":
    action = command.split("|")[0]

    if action == "Add":
        pieces_and_info = add(command)
    elif action == "Remove":
        pieces_and_info = remove(command)
    elif action == "ChangeKey":
        pieces_and_info = change_key(command)

    command = input()

arranged_pieces = sorted(pieces_and_info.items(), key=lambda kvp: (kvp[0]))

for each_piece in arranged_pieces:
    piece = each_piece[0]
    composer = each_piece[1][0]
    key = each_piece[1][1]
    print(f"{piece} -> Composer: {composer}, Key: {key}")
