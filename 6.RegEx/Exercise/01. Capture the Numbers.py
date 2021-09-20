import fileinput
import re
pattern = r"\d+"

for line in fileinput.input():
    matches = [matched_object.group() for matched_object in re.finditer(pattern, line)]
    if matches:
        print(*matches)


# пак

import fileinput
import re

pattern = r"\d+"
for line in fileinput.input():
    if re.findall(pattern, line):
        print(*re.findall(pattern, line), end=" ")

