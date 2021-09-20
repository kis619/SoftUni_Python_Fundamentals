import re

txt = input()
pattern = r"\b(?P<Day>\d{2})(?P<Separator>[\.\-/])(?P<Month>[A-Z][a-z]{2})(?P=Separator)(?P<Year>\d{4})\b"

valid_dates = re.findall(pattern, txt)
for date in valid_dates:
    print(f"Day: {date[0]}, Month: {date[2]}, Year: {date[3]}")


# или

valid_dates2 = [each_object.groupdict() for each_object in re.finditer(pattern, txt)]
for each_date in valid_dates2:
    del each_date["Separator"]
    for k, v in each_date.items():
        print(f"{k}: {v}", end=', ') # не ми се занимава да махам запетайката
    print()

# или
valid_dates3 = [each_object.groupdict() for each_object in re.finditer(pattern, txt)]
dates = [f"Day: {date['Day']}, Month: {date['Month']}, Year: {date['Year']}"for date in valid_dates3]

print("\n".join(dates))


# или
import re

given_dates = input()
pattern = r"(?P<Day>\d{2})(?P<Sep>[\.\-/])(?P<Month>[A-Z][a-z]{2})(?P=Sep)(?P<Year>\d{4}\b)"

matches = [matched_object.groupdict() for matched_object in re.finditer(pattern, given_dates)]
for each_match in matches:
    print(f"Day: {each_match['Day']}, Month: {each_match['Month']}, Year: {each_match['Year']}")

