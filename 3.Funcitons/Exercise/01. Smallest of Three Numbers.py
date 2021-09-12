# Write a function which receives three integer numbers and returns the smallest.
# Print the result on the console. Use appropriate name for the function.

def smallest_of_three_nums(num1, num2, num3):
    """receives 3 numbers, returns the smallest"""
    smallest_number = min(num1, num2, num3)
    return smallest_number


number1 = int(input())
number2 = int(input())
number3 = int(input())

smallest_num = smallest_of_three_nums(number1, number2, number3)
print(smallest_num)