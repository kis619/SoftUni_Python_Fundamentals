import re

information_string = input()
pattern = r"(\||#)(?P<food_item>[a-zA-Z\s]+)\1(?P<expiration_day>\d{2}/\d{2}/\d{2})\1(?P<calories>(\d{1,4}|10000))\1"
matches = [matched_object.groupdict() for matched_object in re.finditer(pattern, information_string)]

calories = 0
for match in matches:
    calories += int(match['calories'])

days_with_food = calories // 2000

print(f"You have food to last you for: {days_with_food} days!")

for each_match in matches:
    print(f"Item: {each_match['food_item']}, Best before: {each_match['expiration_day']}, Nutrition: {each_match['calories']}")

