n = int(input())
key_word = input()

all_items = []
for _ in range(n):
    entry = input()
    all_items.append(entry)
print(all_items)

for i in range(len(all_items) -1, -1, -1):
    element = all_items[i]
    if key_word not in element:
        all_items.remove(element)
print(all_items)

