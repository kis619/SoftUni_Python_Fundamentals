def odd_even_sums(number):
    odd_sum = 0
    even_sum = 0

    for each_char in number:
        numeric_value = int(each_char)
        if numeric_value % 2 == 0:
            even_sum += numeric_value
        else:
            odd_sum += numeric_value
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()
print(odd_even_sums(number))