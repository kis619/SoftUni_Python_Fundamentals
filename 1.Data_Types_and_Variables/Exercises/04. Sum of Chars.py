number_of_lines = int(input())
sum = 0
for x in range(number_of_lines):
    letter = input()
    sum += ord(letter)
print(f"The sum equals: {sum}")

# number_of_lines = int(input())
# sum = 0
# for x in range(number_of_lines):
#     sum += ord((input()))
# print(f"The sum equals: {sum}")