# You will receive a single number n
# On the next n lines you will receive names of courses. You should create a list of courses and print it.
n = int(input())
list_of_courses = []

for _ in range(n):
    list_of_courses.append(input())
print(list_of_courses)