# 6.	Survival of the Biggest
# Write a program that receives a list of integer numbers (separated by a single space) and a number n.
# The number n represents the count of numbers to remove from the list.
# You should remove the smallest ones and then,
# you should print all the numbers that are left in the list, separated by a comma and a space ", ".
string_of_numbers = input()
number_to_be_removed = int(input())
mmy_list = string_of_numbers.split(" ")
new_list = []
for each_element in mmy_list:                           # for i in range(len(mmy_list)):
    element_of_new_list = int(each_element)             # mmy_list[i] = int(mmy_list[i])
    new_list.append(element_of_new_list)

for _ in range(number_to_be_removed):
    new_list.remove(min(new_list))

# for each_element in range(len(new_list)):
#     if each_element == len(new_list) - 1:
#         print(new_list[each_element], end="")
#     else:
#         print(new_list[each_element], end=", ")

for i in range(len(new_list)):
    new_list[i] = str((new_list[i]))
print(", ".join(new_list))

