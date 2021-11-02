import re

emojies_text = input()
pattern = r"(?<=(::|\*\*))[A-Z][a-z]{2,}(?=\1)"

cool_threshold = 1
for char in emojies_text:
    if char.isdigit():
        char = int(char)
        cool_threshold *= char

emojis = [emoji.group() for emoji in re.finditer(pattern, emojies_text)]

cool_emojis = []
uncool_emojis = []
for emoji in emojis:
    coolness = 0
    for char in emoji:
        coolness += ord(char)
    if coolness >= cool_threshold:
        cool_emojis.append(emoji)
    else:
        uncool_emojis.append(emoji)

raw_pattern = r"(::|\*\*)[A-Z][a-z]{2,}\1"
for emoji in uncool_emojis:
    if emoji in emojies_text:
        emojies_text = emojies_text.replace(emoji, "")

emojis_raw = [emoji.group() for emoji in re.finditer(raw_pattern, emojies_text)]

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
if cool_emojis:
    print(*emojis_raw, sep=" \n")
