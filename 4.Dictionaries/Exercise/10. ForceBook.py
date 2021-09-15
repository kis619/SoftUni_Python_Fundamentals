# 9 ot 10
# грешно условие - гърми при този инпут:
# Light | Gosho
# Dark | Pesho
# Pesho -> Softuni
# Gosho -> Softuni
# Lumawaroo
def in_the_forces(jedi_name, dictionary):
    for keys, values in dictionary.items():
        if jedi_name in values:
            return True


def existing(side_name, dictionary):
    if side_name in dictionary:
        return True


def changes_sides(jedi_name, side_name, dictionary):
    for key, value in dictionary.items():
        if jedi_name in value:
            value.remove(jedi_name)
            if key not in forces:
                forces[side_name] = []

            forces[side_name].append(jedi_name)
            break


forces = {}

command = input()
while not command == "Lumpawaroo":

    if "|" in command:
        side, jedi = command.split(" | ")
        if not existing(side, forces) and not in_the_forces(jedi, forces):
            forces[side] = [jedi]
        elif not in_the_forces(jedi, forces):
            forces[side].append(jedi)
        else:
            pass

    elif "->" in command:
        jedi, side = command.split(" -> ")
        if in_the_forces(jedi, forces):
            changes_sides(jedi, side, forces)

        elif not in_the_forces(jedi, forces) and not existing(side, forces):
            forces[side] = [jedi]
        else:
            forces[side].append(jedi)
        print(f"{jedi} joins the {side} side!")

    command = input()


sorted_forces = sorted(forces.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

for side, members in sorted_forces:
    if len(members) > 0:
        print(f"Side: {side}, Members: {len(members)}")

        for member in sorted(members):
            print("! " + member)