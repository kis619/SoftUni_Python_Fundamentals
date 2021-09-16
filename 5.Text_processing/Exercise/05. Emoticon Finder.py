txt = input()

for char in range(len(txt)):
    if txt[char] == ":":
        emoticon = txt[char] + txt[char + 1]
        print(emoticon)