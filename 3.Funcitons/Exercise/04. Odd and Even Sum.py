# You will receive a single number.
# You should write a function that returns the sum of all even and the sum of all odd digits in the given number as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.

def odd_even_sums(num):
    odd_sum = 0
    even_sum = 0
    length_number = len(str(num))
    for _ in range(length_number):
        last_digit = num % 10
        if not last_digit % 2 == 0:
            odd_sum += last_digit
        else:
            even_sum += last_digit
        num = num // 10
    return print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


number = int(input())
odd_even_sums(number)