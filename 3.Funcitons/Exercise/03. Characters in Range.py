# Write a function which receives two characters
# and returns a single string with all the characters in between them (according to the ASCII code),
# separated by a single space. Print the result on the console.

# range 0 - 127

def chars_in_between(char1, char2):
    """receives two characters,
       returns all chars in between
       separated by a single space"""
    ascii_numeric_value1 = ord(char1)
    ascii_numeric_value2 = ord(char2)
    char_list = []
    for numeric_value in range(ascii_numeric_value1 + 1, ascii_numeric_value2):
        char = chr(numeric_value)
        char_list.append(char)
    char_string = " ".join(char_list)
    return char_string


initial_character = input()
final_character = input()

print(chars_in_between(initial_character, final_character))



