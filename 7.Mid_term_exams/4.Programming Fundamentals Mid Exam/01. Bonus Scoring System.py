from math import ceil
students = int(input())
lectures = int(input())
bonus = int(input())

max_points = 0
attended_lectures_by_top_student = 0
for _ in range(students):
    attendance = int(input())
    total_points = attendance / lectures * (5 + bonus)
    if total_points > max_points:
        max_points = total_points
        attended_lectures_by_top_student = attendance

print(f"Max Bonus: {ceil(max_points)}.")
print(f"The student has attended {attended_lectures_by_top_student} lectures.")
