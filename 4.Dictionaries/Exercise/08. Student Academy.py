students_and_grades = {}

pairs_of_rows = int(input())
for _ in range(pairs_of_rows):
    student, grade = input(), float(input())

    if student not in students_and_grades:
        students_and_grades[student] = []
    students_and_grades[student].append(grade)

students_passed = {k: sum(v) / len(v) for k, v in students_and_grades.items() if sum(v) / len(v) >= 4.5}
students_passed_sorted = sorted(students_passed.items(), key=lambda kvp: kvp[1], reverse=True)

for key, value in students_passed_sorted:
    print(f"{key} -> {value:.2f}")
