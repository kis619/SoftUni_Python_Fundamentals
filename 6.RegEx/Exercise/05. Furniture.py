import re

pattern = r"^>>(?P<Item>[a-zA-Z]+)<<(?P<Price>\d+\.?\d+)!(?P<Quantity>\d+)\b"
bought_items = []
total_money_spent = 0

information = input()
while not information == "Purchase":
    item_info = [bought_item.groupdict() for bought_item in re.finditer(pattern, information)]

    for each_match in item_info:
        bought_items.append(each_match["Item"])
        total_money_spent += float(each_match["Price"]) * int(each_match["Quantity"])

    information = input()

print("Bought furniture:")
if bought_items:
    print(*bought_items, sep="\n")
print(f"Total money spend: {total_money_spent:.2f}")