# 6.	Survival of the Biggest
# Write a program that receives a list of integer numbers (separated by a single space) and a number n.
# The number n represents the count of numbers to remove from the list.
# You should remove the smallest ones and then,
# you should print all the numbers that are left in the list, separated by a comma and a space ", ".

list_of_numbers = input().split()
numbers_to_be_removed = int(input())

for i in range(len(list_of_numbers)):
    list_of_numbers[i] = int(list_of_numbers[i])

for _ in range(numbers_to_be_removed):
    list_of_numbers.remove(min(list_of_numbers))

for j in range(len(list_of_numbers)):
    list_of_numbers[j] = str(list_of_numbers[j])

print(", ".join(list_of_numbers))