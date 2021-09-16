strings = input().split()

first_word = strings[0]
second_word = strings[1]
shorter_word = min(len(strings[0]), len(strings[1]))
longer_word = sorted(strings, key=len)[1]
total_sum = 0

for _ in range(shorter_word):
    total_sum += (ord(first_word[_]) * ord((second_word[_])))

remaining_char = longer_word[shorter_word:]
for char in remaining_char:
    total_sum += ord(char)

print(total_sum)