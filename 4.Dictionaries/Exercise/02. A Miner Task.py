inventory = {}

resource = input()
while not resource == "stop":
    if resource not in inventory:
        inventory[resource] = 0

    quantity = int(input())
    inventory[resource] += quantity

    resource = input()

for key, value in inventory.items():
    print(f"{key} -> {value}")
