key_materials = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
backpack = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}

items = input().split()

enough_resources = False
while not enough_resources:

    for item in range(0, len(items), 2):
        quantity = int(items[item])
        material = items[item + 1].lower()

        if material in backpack:
            backpack[material] += quantity
            if backpack[material] >= 250:
                backpack[material] -= 250
                print(key_materials[material] + " obtained!")
                enough_resources = True
                break
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += quantity

    if enough_resources:
        break

    items = input().split()

backpack = sorted(backpack.items(), key=lambda kvp: (-kvp[1], kvp[0]))
junk = sorted(junk.items(), key=lambda kvp: kvp[0])
print(backpack)
print(junk)
for key, value in backpack:
    print(f"{key}: {value}")
for key, value in junk:
    print(f"{key}: {value}")