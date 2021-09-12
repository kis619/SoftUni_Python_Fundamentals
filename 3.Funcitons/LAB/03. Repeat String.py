# Write a function which receives a string and a counter n.
# The function should return a new string – the result of repeating the old string n times.
# Print the result of the function. Try using lambda.

def multiply_string(string, counter):
    """receives a string and a number, multiplies them"""
    return string * counter


received_string = input()
received_counter = int(input())
print(multiply_string(received_string, received_counter))
