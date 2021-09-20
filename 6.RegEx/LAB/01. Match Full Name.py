import re

txt = input()
patter = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

print(" ".join(re.findall(patter, txt)))


# another

import re
txt = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

print(*re.findall(pattern, txt), sep="хуй")