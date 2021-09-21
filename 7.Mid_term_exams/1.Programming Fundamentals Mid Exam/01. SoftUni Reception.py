employee1_handles_these_students = int(input())
employee2_handles_these_students = int(input())
employee3_handles_these_students = int(input())
all_employees = employee3_handles_these_students + employee2_handles_these_students + employee1_handles_these_students
students_count = int(input())

count = 0

while students_count > 0:
    students_count -= all_employees
    count += 1
    if count % 4 == 0:
        count += 1


print(f"Time needed: {count}h.")


######################################
# woks but better logic should be applied