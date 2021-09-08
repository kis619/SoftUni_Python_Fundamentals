# You will receive a number n and a word. On the next n lines you will be given some strings.
# You should add them in a list and print them.
# After that you should filter out only the strings that include the given word and print that list too.
n = int(input())
word = input()

all_items = []
keyword_items = []
for _ in range(n):
    entry = input()
    all_items.append(entry)
    if word in entry:
        keyword_items.append(entry)
print(all_items)
print(keyword_items)