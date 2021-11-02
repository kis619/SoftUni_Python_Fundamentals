def plunder(command, cities_list):
    town, people, gold = command[1:]
    people, gold = int(people), int(gold)

    cities_list[town]["Population"] -= people
    cities_list[town]["Gold"] -= gold
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

    if cities_list[town]["Population"] <= 0 or cities_list[town]["Gold"] <= 0:
        print(f"{town} has been wiped off the map!")
        del cities_list[town]

    # return cities_list


def prosper(command, cities_list):
    town, gold = command[1:]
    gold = int(gold)
    if not gold < 0:
        cities_list[town]["Gold"] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities_list[town]['Gold']} gold.")
    else:
        print("Gold added cannot be a negative number!")


cities = {}

information = input()
while not information == "Sail":
    city, population, gold = information.split('||')
    population, gold = int(population), int(gold)

    if city not in cities:
        cities[city] = {"Population": 0, "Gold": 0}
    cities[city]["Population"] += population
    cities[city]["Gold"] += gold

    information = input()

new_information = input()
while not new_information == "End":
    all_elements = new_information.split("=>")
    event = all_elements[0]

    if event == "Plunder":
        plunder(all_elements, cities)
    elif event == "Prosper":
        prosper(all_elements, cities)

    new_information = input()

cities_left_sorted = sorted(cities.items(), key=lambda kvp: (-kvp[1]["Gold"], kvp[0]))

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, properties in cities_left_sorted:
        print(f"{city} -> Population: {properties['Population']} citizens, Gold: {properties['Gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
