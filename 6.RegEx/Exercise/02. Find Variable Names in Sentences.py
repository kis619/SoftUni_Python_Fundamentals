import re

pattern = r"(?<=( _))[a-zA-Z0-9]+\b"
txt = input()

valid = [matched_object.group() for matched_object in re.finditer(pattern, txt)]

print(",".join(valid))

# пак

import re

pattern = r"(?<= _)[a-zA-Z\d]+\b"
print(*re.findall(pattern, input()), sep=",")