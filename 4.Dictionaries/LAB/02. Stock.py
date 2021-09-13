products_and_quantities = input().split()
searched_products = list(input().split())

inventory = {}

for i in range(0, len(products_and_quantities), 2):
    product = products_and_quantities[i]
    quantity = int(products_and_quantities[i + 1])
    inventory[product] = quantity

for given_product in searched_products:
    if given_product in inventory:
        print(f"We have {inventory[given_product]} of {given_product} left")
    else:
        print(f"Sorry, we don't have {given_product}")