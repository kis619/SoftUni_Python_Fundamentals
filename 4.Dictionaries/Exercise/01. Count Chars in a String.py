given_string = "".join(input().split())

dictionary = {}

for char in given_string:
    if char not in dictionary:
        dictionary[char] = 0
    dictionary[char] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")