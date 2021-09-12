# Write a function that receives two integer numbers. Calculate factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.

def divide_two_factorials(num1, num2):
    factorial1 = 1
    for i in range(1, num1 + 1):
        factorial1 *= i
    factorial2 = 1
    for j in range(1, num2 + 1):
        factorial2 *= j
    divided = factorial1 / factorial2
    return print(f"{divided:.2f}")


number1 = int(input())
number2 = int(input())
divide_two_factorials(number1, number2)





