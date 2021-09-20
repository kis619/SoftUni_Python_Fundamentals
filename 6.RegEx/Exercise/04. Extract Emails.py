import re

regex_pattern = r"(^|(?<=\s))[a-zA-Z\d]+[a-zA-Z\d\.\-_]*@[a-z]+(\-([a-z]+))?((\.[a-z-]+)(?!\-)\b)+"
txt = input()

[print(el.group()) for el in re.finditer(regex_pattern, txt)]