# Create a function which receives three parameters, calculates a result depending on the given operator and returns it.
# Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers.
# The operator can be one of the following:  'multiply', 'divide', 'add', 'subtract'.
def calculate(operator, number1, number2):
    """receives an operator and three numbers
       and performs the operation"""

    if operator == "multiply":
        return number1 * number2
    if operator == "divide":
        return number1 // number2
    if operator == "add":
        return number1 + number2
    if operator == "subtract":
        return number1 - number2


given_operator = input()
num1 = int(input())
num2 = int(input())

print(calculate(given_operator, num1, num2))