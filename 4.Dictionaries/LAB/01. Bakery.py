items = input().split()
products_dict = {}

for index in range(0, len(items), 2):
    product = items[index]
    quantity = int(items[index + 1])
    products_dict[product] = quantity

print(products_dict)
