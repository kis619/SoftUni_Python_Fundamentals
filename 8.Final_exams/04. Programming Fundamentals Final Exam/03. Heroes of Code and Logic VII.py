def cast_spell(given_command, heroes_list):
    command_name, hero_name, mana_needed, spell_name = given_command.split(" - ")
    mana_needed = int(mana_needed)

    if heroes_list[hero_name]["MP"] >= mana_needed:
        heroes_list[hero_name]["MP"] -= mana_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_list[hero_name]['MP']} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")


def take_damage(given_command, heroes_list):
    command_name, hero_name, damage, attacker = given_command.split(" - ")

    heroes_list[hero_name]["HP"] -= int(damage)
    if heroes_list[hero_name]["HP"] > 0:
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_list[hero_name]['HP']} HP left!")
    else:
        print(f"{hero_name} has been killed by {attacker}!")
        del heroes_list[hero_name]


def recharge(given_command, heroes_list):
    command_name, hero_name, amount = given_command.split(" - ")
    amount = int(amount)
    heroes_list[hero_name]['MP'] += amount

    if heroes_list[hero_name]['MP'] > 200:
        amount -= (heroes_list[hero_name]['MP'] - 200)
        heroes_list[hero_name]['MP'] = 200

    print(f"{hero_name} recharged for {amount} MP!")


def heal(given_command, heroes_list):
    command_name, hero_name, amount = given_command.split(" - ")
    amount = int(amount)
    heroes_list[hero_name]['HP'] += amount

    if heroes_list[hero_name]['HP'] > 100:
        amount -= (heroes_list[hero_name]['HP'] - 100)
        heroes_list[hero_name]['HP'] = 100

    print(f"{hero_name} healed for {amount} HP!")


n = int(input())

heroes = {}
for _ in range(n):
    hero, hit_points, mana = input().split()
    heroes[hero] = {"HP": int(hit_points), "MP": int(mana)}

command = input()
while not command == "End":
    command_info = command.split(" - ")
    action = command_info[0]

    if action == "CastSpell":
        cast_spell(command, heroes)
    elif action == "TakeDamage":
        take_damage(command, heroes)
    elif action == "Recharge":
        recharge(command, heroes)
    elif action == "Heal":
        heal(command, heroes)

    command = input()

sorted_heroes = sorted(heroes.items(), key=lambda kvp: (-kvp[1]["HP"], kvp[0]))

for hero, properties in sorted_heroes:
    print(f"{hero}")
    print(f" HP: {properties['HP']}")
    print(f" MP: {properties['MP']}")
