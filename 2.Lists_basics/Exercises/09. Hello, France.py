collection_of_items = input().split("|")
budget = float(input())
prices_list = []
money_spent = 0
for each_cell in collection_of_items:
    individual_item = each_cell.split("->")
    item_type = individual_item[0]
    item_price = float(individual_item[1])
    if item_price > budget:
        continue
    if (item_type == "Clothes" and item_price <= 50.00) or\
       (item_type == "Shoes" and item_price <= 35.00) or\
       (item_type == "Accessories" and item_price <= 20.50):
        budget -= item_price
        money_spent += item_price
        new_price = item_price + .4 * item_price
        prices_list.append(new_price)
profit = .4 * money_spent

for each_item in range(len(prices_list)):
    if each_item == len(prices_list) - 1:
        print(f"{prices_list[each_item]:.2f}")
    else:
        print(f"{prices_list[each_item]:.2f}", end=" ")
print(f"Profit: {profit:.2f}")
if budget + money_spent + profit >= 150:
    print("Hello, France!")
else:
    print("Time to go.")