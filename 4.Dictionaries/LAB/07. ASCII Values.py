list_characters = list(input().split(", "))
dictionary = {el: ord(el) for el in list_characters}
print(dictionary)