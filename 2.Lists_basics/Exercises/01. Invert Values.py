# Write a program which receives a single string containing numbers separated by a single space.
# Print a list containing the opposite of each number.

string = input()
my_list = string.split(" ")
new_list = []
for each_position in range((len(my_list))):
    number = int(my_list[each_position])
    if number > 0:
        number = - number
        new_list.append(number)
    elif number < 0:
        number = - number
        new_list.append(number)
    elif number == 0:
        new_list.append(number)
print(new_list)

