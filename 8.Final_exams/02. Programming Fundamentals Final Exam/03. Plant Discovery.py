n = int(input())

plants = {}

for _ in range(n):
    plant_name, rarity = input().split("<->")
    # rarity = int(rarity)
    plants[plant_name] = {'rarity': int(rarity), 'ratings': []}

data = input()
while not data == "Exhibition":
    command, command_params = data.split(": ")
    try:
        if command == "Rate":
            plant_name, rating = command_params.split(" - ")
            # rating = int(rating)
            plants[plant_name]["ratings"].append(int(rating))
        elif command == "Update":
            plant_name, rarity = command_params.split(" - ")
            # rarity = int(rarity)
            plants[plant_name]["rarity"] = int(rarity)
        elif command == "Reset":
            plant_name = command_params
            plants[plant_name]["ratings"].clear()
        else:
            print("error")

    except KeyError:
        print("error")

    data = input()

for plant, data in plants.items():
    plants[plant]["ratings"] = sum(plants[plant]["ratings"]) / len(plants[plant]["ratings"])


sorted_plants = sorted(plants.items(), key=lambda tkvp: (-tkvp[1]["rarity"], -tkvp[1]["ratings"]))

print("Plants for the exhibition:")
for each_plant in sorted_plants:
    print(f"- {each_plant[0]}; Rarity: {each_plant[1]['rarity']}; Rating: {each_plant[1]['ratings']:.2f}")
