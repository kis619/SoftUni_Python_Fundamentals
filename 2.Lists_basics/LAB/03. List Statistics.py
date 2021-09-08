# You will be given a number n. On the next n lines you will receive integers. You should create and print two lists:
# •	One with all the positives (including 0) numbers
# •	One with all the negatives numbers
# Finally, print the following message: "Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}"
n = int(input())
positive_numbers = []
negative_numbers = []

for _ in range(n):
    current_number = int(input())
    if current_number >= 0:
        positive_numbers.append(current_number)
    else:
        negative_numbers.append(current_number)
count_of_positives = len(positive_numbers)
sum_of_negatives = sum(negative_numbers)

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {count_of_positives}. Sum of negatives: {sum_of_negatives}")