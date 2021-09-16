banned_word = input()
string_of_words = input()

while banned_word in string_of_words:
    string_of_words = string_of_words.replace(banned_word, "")
print(string_of_words)