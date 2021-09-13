# def print_list(my_dick):
#     for el in my_dict:
#         print(f"- {el}: {my_dict[el]}")


information = input()
my_dict = {}

while not information == "statistics":
    food_info = information.split(": ")
    product = food_info[0]
    quantity = int(food_info[1])
    if product not in my_dict:
        my_dict[product] = quantity
    else:
        my_dict[product] += quantity
    information = input()

print("Products in stock:")
for el in my_dict:     # print_list(my_dict)
    print(f"- {el}: {my_dict[el]}")
print(f"Total Products: {len(my_dict)}\n"
      f"Total Quantity: {sum(my_dict.values())}")



