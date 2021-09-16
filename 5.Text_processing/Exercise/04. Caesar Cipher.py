phrase = input()

for char in phrase:
    new_char = chr(ord(char) + 3)
    print(new_char, end="")