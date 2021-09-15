def already_registered (username, registered_cars):
    if username in registered_cars:
        return True
    return False


number_of_lines = int(input())
currently_registered_ppl = {}

for _ in range(number_of_lines):
    command_and_cust_info = input().split()
    command = command_and_cust_info[0]
    user_name = command_and_cust_info[1]

    if command == "register":
        license_plate = command_and_cust_info[2]
        if already_registered(user_name, currently_registered_ppl):
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            currently_registered_ppl[user_name] = license_plate
            print(f"{user_name} registered {license_plate} successfully")

    else:
        if already_registered(user_name, currently_registered_ppl):
            del currently_registered_ppl[user_name]
            print(user_name + " unregistered successfully")
        else:
            print(f"ERROR: user {user_name} not found")

for key, value in currently_registered_ppl.items():
    print(f"{key} => {value}")

