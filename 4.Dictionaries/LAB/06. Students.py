information = input()
dictionary = {}
while ":" in information:
    id_info = information.split(":")[1]
    name = information.split(":")[0]
    course = information.split(":")[2]
    dictionary[id_info] = [name, course]
    information = input()

if "_" in information:
    information = information.replace("_", " ")

for key, value in dictionary.items():
    if information in value:
        print(f"{value[0]} - {key}")