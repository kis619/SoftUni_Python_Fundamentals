cells_statistics = input().split('#')
water = int(input())
total_fire = 0
effort = 0
list_of_cells = []
for each_cell in cells_statistics:
    cell = each_cell.split(" = ")
    fire_type = cell[0]
    numeric_value = int(cell[1])
    if water < numeric_value:
        continue
    if (fire_type == "High" and 81 <= numeric_value <= 125) or\
       (fire_type == "Medium" and 51 <= numeric_value <= 80) or\
       (fire_type == "Low" and 1 <= numeric_value <= 50):
        water -= numeric_value
        total_fire += numeric_value
        effort += numeric_value * .25
        list_of_cells.append(f" - {numeric_value}")

print("Cells:")
for i in range(len(list_of_cells)):
    print(list_of_cells[i])
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")


