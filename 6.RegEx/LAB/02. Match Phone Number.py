import re

txt = input()
pattern = r"\+359([ |-])2\1\d{3}\1\d{4}\b"

print(", ".join([obj.group() for obj in re.finditer(pattern, txt)]))


# another
import re

phone_numbers = input()
pattern = r"\+359(?P<separator>( |-))2(?P=separator)\d{3}(?P=separator)\d{4}\b"

correct_numbers = [matched_object.group() for matched_object in re.finditer(pattern, phone_numbers)]
print(*correct_numbers, sep=", ")