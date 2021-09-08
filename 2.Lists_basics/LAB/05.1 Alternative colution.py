# You will receive a single number n. On the next n lines you will receive integers. After that you will be given one of the following commands:
# •	even
# •	odd
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

n = int(input())
even_list = []
odd_list = []
negative_list = []
positive_list = []

for _ in range(n):
    number = int(input())
    if number % 2 == 0:
        even_list.append(number)
        if number >= 0:
            positive_list.append(number)
        else:
            negative_list.append(number)
    else:
        odd_list.append(number)
        if number >= 0:
            positive_list.append(number)
        else:
            negative_list.append(number)

command = input()

if command == "even":
    print(even_list)
elif command == "odd":
    print(odd_list)
elif command == "negative":
    print(negative_list)
else:
    print(positive_list)


