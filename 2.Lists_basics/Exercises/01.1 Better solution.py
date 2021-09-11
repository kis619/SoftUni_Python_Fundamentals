string = input().split()

inverted_string = []

for each_item in string:
    inverted_value = int(each_item) * -1
    inverted_string.append(inverted_value)

print(inverted_string)