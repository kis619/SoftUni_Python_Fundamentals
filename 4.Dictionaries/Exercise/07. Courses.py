courses = {}

info = input()
while not info == "end":
    course, student = info.split(" : ")

    if course not in courses:
        courses[course] = []
    courses[course].append(student)

    info = input()


sorted_by_number_of_students = sorted(courses.items(), key=lambda kvp: -len(kvp[1]))

for key, value in sorted_by_number_of_students:
    print(f"{key}: {len(value)}")
    value = sorted(value)
    for index in range(len(value)):
        print(f"-- {value[index]}")



