number_of_snowballs = int(input())
best_snowball = 0
best_snow = 0
best_time = 0
top_quality = 0
for snowballs in range(1, number_of_snowballs + 1):
    snow = int(input())
    time = int(input())
    quality = int(input())
    value = (snow/time) ** quality
    if value > best_snowball:
        best_snowball = value
        best_snow = snow
        best_time = time
        top_quality = quality
print(f"{best_snow} : {best_time} = {int(best_snowball)} ({top_quality})")