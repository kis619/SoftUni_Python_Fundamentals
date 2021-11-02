import re


def clean_special_symbols(word1, word2):
    special_symbols = ["#", "@"]
    for symbol in special_symbols:
        if symbol in word1:
            word1 = word1.replace(symbol, "")
            word2 = word2.replace(symbol, "")
            break
    cleaned_words = (word1, word2)
    return cleaned_words


given_string = input()
pattern = r"(@|#)[a-zA-Z]{3,}\1\1[a-zA-Z]{2,}\1"

matches = [each_match.group() for each_match in re.finditer(pattern, given_string)]


mirror_words = []
for each_pair in matches:
    half_of_word = len(each_pair) // 2
    first_word = each_pair[:half_of_word]
    second_word = each_pair[half_of_word:]
    if first_word == second_word[::-1]:
        mirror_words.append(clean_special_symbols(first_word, second_word))

number_of_matches = len(matches)

if not number_of_matches:
    print("No word pairs found!")
else:
    print(f"{number_of_matches} word pairs found!")

if not mirror_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    to_print = []
    for each_pair in mirror_words:
        to_print.append(f"{each_pair[0]} <=> {each_pair[1]}")
    print(*to_print, sep=", ")



