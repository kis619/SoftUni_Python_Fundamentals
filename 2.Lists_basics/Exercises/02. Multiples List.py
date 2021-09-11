# Write a program that receives two numbers (factor and count) and creates
# a list with length of the given count and contains only integer numbers that are multiples of the given factor.
# The numbers should be only positive, and they should be arranged in ascending order,
# starting from the smallest multiple number.

factor = int(input())
count = int(input())
number = 0
my_list = []
for _ in range(count):
    number += factor
    my_list.append(number)
print(my_list)