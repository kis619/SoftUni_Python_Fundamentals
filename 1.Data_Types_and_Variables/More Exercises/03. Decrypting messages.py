key = int(input())
number_of_lines = int(input())
message = []
for each_line in range(number_of_lines):
    numeric_value_of_character = ord(input()) + key
    message.append(chr(numeric_value_of_character))
for i in message:
    print(i, end="")


