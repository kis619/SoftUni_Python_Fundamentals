def drive(command_info, car_list):
    useless, car, distance, fuel = command_info.split(" : ")
    distance, fuel = int(distance), int(fuel)

    if car_list[car]["Fuel"] < fuel:
        print("Not enough fuel to make that ride")
    else:
        car_list[car]["Fuel"] -= fuel
        car_list[car]["Mileage"] += distance
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

    if car_list[car]["Mileage"] >= 100000:
        print(f"Time to sell the {car}!")
        del car_list[car]

    return car_list


def refuel(command_info, car_list):
    useless, car, fuel = command_info.split(" : ")
    fuel = int(fuel)
    fuel_in_car = car_list[car]["Fuel"]
    fuel_needed = 75 - fuel_in_car
    car_list[car]["Fuel"] += fuel

    if car_list[car]["Fuel"] > 75:
        left_fuel = car_list[car]["Fuel"] - 75
        fuel -= left_fuel
        car_list[car]["Fuel"] = 75

    print(f"{car} refueled with {fuel} liters")

    return car_list


def revert(command_info, car_list):
    useless, car, kilometers = command_info.split(" : ")
    kilometers = int(kilometers)
    car_list[car]["Mileage"] -= kilometers

    if car_list[car]["Mileage"] < 10000:
        car_list[car]["Mileage"] = 10000
    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")

    return car_list


number_of_cars = int(input())

cars = {}
for _ in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    cars[car] = {"Mileage": int(mileage), "Fuel": int(fuel)}

command = input()
while not command == "Stop":
    command_specifics = command.split(" : ")
    action = command_specifics[0]

    if action == "Drive":
        cars = drive(command, cars)
    elif action == "Refuel":
        cars = refuel(command, cars)
    elif action == "Revert":
        cars = revert(command, cars)

    command = input()

sorted_car_list = sorted(cars.items(), key=lambda kvp: (-kvp[1]["Mileage"], kvp[0]))

for each_car, measures in sorted_car_list:
    print(f"{each_car} -> Mileage: {measures['Mileage']} kms, Fuel in the tank: {measures['Fuel']} lt.")

# for each_car in sorted_car_list:
#     print(f"{each_car[0]} -> Mileage: {each_car[1]['Mileage']} kms, Fuel in the tank: {each_car[1]['Fuel']} lt.")