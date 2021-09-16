txt = input()

emoji = [print(f"{txt[index]}{txt[index + 1]}") for index in range(len(txt)) if txt[index] == ":"]
