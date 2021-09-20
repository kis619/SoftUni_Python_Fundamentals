import re

pattern = r"^>>(?P<item_name>[a-zA-Z]+)<<(?P<price>\d+\.?\d+)!(?P<quantity>\d+)($|(?=\s))"
bought_items = []
total_money_spent = 0

information = input()
while not information == "Purchase":
    match = re.match(pattern, information)

    if match:
        bought_items.append(match["item_name"])
        total_money_spent += float(match["price"]) * int(match["quantity"])

    information = input()

print("Bought furniture:")
if bought_items:
    print("\n".join(bought_items))
print(f"Total money spend: {total_money_spent:.2f}")

