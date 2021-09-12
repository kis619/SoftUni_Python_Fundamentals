# You will receive three integer numbers.
# Write functions named:
# •	sum_numbers() which returns the sum of the first two integers
# •	subtract() which returns the difference between the returned result of the first function and the third integer.
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
# Print the result of the subtract() function on the console.

def sum_numbers(num1, num2):
    """receives two numbers, returns their sum"""
    result = num1 + num2
    return result


def subtract(jgkjgkj, num3):
    """receives the result of the first function and another number, returns their difference"""
    result = jgkjgkj - num3
    return result


def add_and_subtract(num1, num2, num3):
    sum1 = sum_numbers(num1, num2)
    return subtract(sum1, num3)


number1 = int(input())
number2 = int(input())
number3 = int(input())

print(add_and_subtract(number1, number2, number3))
