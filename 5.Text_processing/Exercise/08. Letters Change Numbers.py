from string import ascii_lowercase, ascii_uppercase

list_of_combinations = input().split()

total_sum = 0
current_combination_sum = 0

for combination in list_of_combinations:
    first_letter = combination[0]
    second_letter = combination[len(combination) - 1]
    number = int(combination[1:len(combination) - 1])

    if first_letter.isupper():
        position = ascii_uppercase.index(first_letter) + 1
        number /= position
    elif first_letter.islower():
        position = ascii_lowercase.index(first_letter) + 1
        number *= position

    if second_letter.isupper():
        position = ascii_uppercase.index(second_letter) + 1
        number -= position
    elif second_letter.islower():
        position = ascii_lowercase.index(second_letter) + 1
        number += position

    total_sum += number

print(f"{total_sum:.2f}")