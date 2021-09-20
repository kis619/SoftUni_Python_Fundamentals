import re

txt = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

complying_numbers = re.finditer(pattern, txt)

for each_match in complying_numbers:
    print(each_match.group(0), end=" ")

# или
print()
correct_numbers = [matched_object.group() for matched_object in re.finditer(pattern, txt)]
print(*correct_numbers)

# решено пак
import re

given_numbers = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

matches = [matched_object.group() for matched_object in re.finditer(pattern, given_numbers)]
print(*matches)