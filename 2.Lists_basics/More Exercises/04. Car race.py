list_str_numbers = input().split()
list_numbers = [int(x) for x in list_str_numbers]

race_track_length = len(list_numbers)
left_racer_track = list_numbers[0:((race_track_length - 1) // 2)]
right_racer_track = list_numbers[((race_track_length - 1) // 2) + 1:]
finish_line = (race_track_length - 1) // 2 + 1

left_racer_time = 0
for element in left_racer_track:
    if not element == 0:
        left_racer_time += element
    else:
        left_racer_time -= .2 * left_racer_time

right_racer_time = 0
for i in range(len(right_racer_track) - 1, -1, -1):
    racing_lap = right_racer_track[i]
    if not racing_lap == 0:
        right_racer_time += racing_lap
    else:
        right_racer_time -= .2 * right_racer_time

if left_racer_time > right_racer_time:
    print(f"The winner is right with total time: {right_racer_time:.1f}")
else:
    print(f"The winner is left with total time: {left_racer_time:.1f}")
