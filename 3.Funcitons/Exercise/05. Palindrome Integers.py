# A palindrome is a number which reads the same backward as forward, such as 323 or 1001.
# Write a function which receives a list of positive integers, separated by comma and space ", ".
# The function should check if each integer is a palindrome - True or False. Print the result.
def palindrome(number):
    length_number = len(str(number))
    list_of_digits = []
    reversed_list_of_digits = []
    for i in range(length_number):
        last_digit = number % 10
        number = number // 10
        list_of_digits.append(last_digit)
        reversed_list_of_digits.append(last_digit)
    reversed_list_of_digits.reverse()
    is_palindrome = True
    if not list_of_digits == reversed_list_of_digits:
        is_palindrome = False
    return is_palindrome


list_integers = input().split(", ")

for each_element in list_integers:
    print(palindrome(int(each_element)))