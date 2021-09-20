import fileinput
import re

pattern = r"www\.[a-zA-Z\d-]+(\.[a-z]+)+"

for line in fileinput.input():
    matches = [matched_object.group() for matched_object in re.finditer(pattern, line)]
    if matches:
        print(*matches)


# друг

import re
import fileinput

pattern = r"www\.[a-zA-Z\d\-]+(\.[a-z]+){1,}"

for line in fileinput.input():
    [print(el.group()) for el in re.finditer(pattern, line)]