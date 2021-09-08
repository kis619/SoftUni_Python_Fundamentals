# You will receive a single number n. On the next n lines you will receive integers. After that you will be given one of the following commands:
# •	even
# •	odd
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

n = int(input())
my_list = []
for _ in range(n):
    number = int(input())
    my_list.append(number)
command = input()
if command == "even":
    for each_number in range(len(my_list) -1 , -1, -1):
        number = my_list[each_number]
        if number % 2 == 1:
            my_list.remove(number)
elif command == "odd":
    for each_number in range(len(my_list) -1, -1, -1):
        number = my_list[each_number]
        if number % 2 == 0:
            my_list.remove(number)
elif command == "negative":
    for each_number in range(len(my_list) - 1, -1, -1):
        number = my_list[each_number]
        if number >= 0:
            my_list.remove(number)
elif command == "positive":
    for each_number in range(len(my_list) - 1, -1, -1):
        number = my_list[each_number]
        if number < 0:
            my_list.remove(number)
print(my_list)