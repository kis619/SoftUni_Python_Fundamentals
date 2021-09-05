number = int(input())

# 97 - 122

for i in range(1, number + 1):
    character = chr(96 + i)
    for x in range(1, number + 1):
        character2 = chr(96 + x)
        for y in range(1, number + 1):
            character3 = chr(96 + y)
            print(character + character2 + character3)
