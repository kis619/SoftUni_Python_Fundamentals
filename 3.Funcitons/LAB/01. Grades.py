# 1.	Grades
# Write a function which receives a grade between 2.00 and 6.00 and prints the corresponding grade in words.
# •	2.00 – 2.99 - "Fail"
# •	3.00 – 3.49 - "Poor"
# •	3.50 – 4.49 - "Good"
# •	4.50 – 5.49 - "Very Good"
# •	5.50 – 6.00 - "Excellent"
# Examples
# Input	Output
# 3.33	Poor
# 4.50	Very Good
# 2.99	Fail

def corresponding_grade(grade):
    """gets numeric value of grade, prints text value"""
    if 2.00 <= grade <= 2.99:
        return "Fail"
    elif grade <= 3.49:
        return "Poor"
    elif grade <= 4.49:
        return "Good"
    elif grade <= 5.49:
        return "Very Good"
    elif grade <= 6.00:
        return "Excellent"


print(corresponding_grade(float(input())))
