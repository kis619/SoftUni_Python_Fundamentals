integers = [int(el) for el in input().split()]

average = sum(integers) / len(integers)

numbers_above_average = [num for num in integers if num > average]
numbers_above_average.sort(reverse=True)
top_5 = [str(numbers_above_average[i]) for i in range(len(numbers_above_average)) if i < 5]

if len(top_5) == 0:
    print("No")
else:
    print(" ".join(top_5))

