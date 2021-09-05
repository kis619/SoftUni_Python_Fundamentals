number = int(input())
for all_numbers in range(1, number + 1):
    str_all_n = str(all_numbers)
    sum = 0
    for each_char in str(all_numbers):
        digit = int(each_char)
        sum += digit
    if sum == 5 or sum == 7 or sum == 11:
        print(f"{all_numbers} -> True")
    else:
        print(f"{all_numbers} -> False")

number = int(input())
for num in range(1, number + 1):
    sum_of_digits = 0
    digits = num
    while digits > 0:
        sum_of_digits += digits % 10
        digits //= 10
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
