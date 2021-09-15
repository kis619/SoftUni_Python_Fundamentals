item = input()
products_prices = {}
products_quantities = {}

while not item == "buy":
    product, price, quantity = item.split()
    price = float(price)
    quantity = int(quantity)

    products_prices[product] = price

    if product not in products_quantities:
        products_quantities[product] = quantity
    else:
        products_quantities[product] += quantity

    item = input()

for key, value in products_prices.items():
    sum_total = value * products_quantities[key]
    print(f"{key} -> {sum_total:.2f}")