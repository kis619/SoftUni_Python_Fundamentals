courses = {}

information = input()
while ":" in information:
    name, student_id, course = information.split(":")

    if course not in courses:
        courses[course] = {}
    courses[course][student_id] = name

    information = input()

if "_" in information:
    information = information.replace("_", " ")

searched_course = information

for name, student_id in courses[searched_course].items():
    print(f"{student_id} - {name}")


