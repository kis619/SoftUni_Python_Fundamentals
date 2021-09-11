numbers = input().split(", ")
new_numbers = []
for j in range(len(numbers)):
    number = int(numbers[j])
    new_numbers.append(number)

for i in range(len(new_numbers)):
    if new_numbers[i] == 0:
        new_numbers.remove(0)
        new_numbers.append(0)

print(new_numbers)
