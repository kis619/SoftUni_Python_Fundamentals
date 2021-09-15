item = input()
orders = {}
while not item == "buy":
    product_info = item.split()
    product = product_info[0]
    price = float(product_info[1])
    quantity = int(product_info[2])
    if product not in orders:
        orders[product] = [price, quantity]
    else:
        orders[product][0] = price
        orders[product][1] += quantity

    item = input()

for key, value in orders.items():
    total_sum = value[0] * value[1]
    print(f"{key} -> {total_sum:.2f}")
