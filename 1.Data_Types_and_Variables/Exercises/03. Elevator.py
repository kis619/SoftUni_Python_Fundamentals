# from math import ceil
# n_of_people = int(input())
# elevator_capacity = int(input())
# courses = ceil(n_of_people / elevator_capacity)
# print(courses)

n_of_people = int(input())
elevator_capacity = int(input())

courses = n_of_people / elevator_capacity
if not n_of_people % elevator_capacity == 0:
    courses += 1
print(int(courses))