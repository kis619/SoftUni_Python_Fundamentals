import re
pattern = r"(?<=(=|/))[A-Z][a-zA-Z]{2,}(?=\1)"

map_locations = input()
valid_locations = [location.group() for location in re.finditer(pattern, map_locations)]

travel_points = sum([len(location) for location in valid_locations])

print(f"Destinations: {', '.join(valid_locations)}")
print(f"Travel Points: {travel_points}")


### Работи, но не е мн готяно решение
# import re
#
# txt = input()
# pattern = r"(=|/)(?P<Location>[A-Z][a-zA-Z]{2,})\1"
#
# matches = [location.groupdict() for location in re.finditer(pattern, txt)]
#
# destinations = []
# travel_points = 0
# for each in matches:
#     for destination in each.values():
#         travel_points += len(destination)
#         destinations.append(destination)
#
# print(f"Destinations: {', '.join(destinations)}")
# print(f"Travel Points: {travel_points}")

