tank_capacity = 255
number_of_refills = int(input())
water_already_added = 0
for each_refill in range(number_of_refills):
    liters_water = int(input())
    water_already_added += liters_water
    if water_already_added > tank_capacity:
        print("Insufficient capacity!")
        water_already_added -= liters_water
print(water_already_added)
