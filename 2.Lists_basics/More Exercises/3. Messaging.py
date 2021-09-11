# On the first line you will receive a sequence of numbers, separated by a single space.
# On the second line you will receive a string with chars.
# Your task is to write a program which sends a message only using chars from the given string.
# Each char the program adds to the message should be found by its index.
# The index you are looking for is the sum of a number's digits from the sequence.
# If the index is greater than the length of the text, continue counting from the beginning (so that you always have a valid index).
# When you find a char, you should add it to the message and remove it from the string.
# It means that for the next index, the text will be with one character less.
# Print the final message.

list_numbers = [int(x) for x in input().split()]
list_of_chars_in_string = [x for x in input()]
index_list = []
for number in list_numbers:
    sum = 0
    number_length = len(str(number))
    for i in range(number_length):
        last_digit = number % 10
        sum += last_digit
        number = number // 10
    index_list.append(sum)

output = []
new_string =""
for i in index_list:
    if i > len(string):
    output.append(string[i])






