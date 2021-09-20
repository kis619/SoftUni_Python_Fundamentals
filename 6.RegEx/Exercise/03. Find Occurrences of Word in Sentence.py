import re

txt = input()
searched_word = input()

pattern = rf"\b{searched_word}\b"

matches = re.findall(pattern, txt, re.IGNORECASE)

print(len(matches))

# пак

import re
text_body = input()
searched_word = input()

regex_pattern = rf"\b{searched_word}\b"

print(len(re.findall(regex_pattern, text_body, re.IGNORECASE)))

