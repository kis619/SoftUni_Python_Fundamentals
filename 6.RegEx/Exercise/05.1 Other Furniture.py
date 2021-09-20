import re

pattern = r"^>>(?P<item_name>[a-zA-Z]+)<<(?P<price>\d+\.?\d+)!(?P<quantity>\d+)\b"
bought_items = []
total_money_spent = 0

information = input()
while not information == "Purchase":
    match = re.findall(pattern, information)

    if match:
        bought_items.append(match[0][0])
        total_money_spent += float(match[0][1]) * int(match[0][2])

    information = input()

print("Bought furniture:")
for each_item in bought_items:
    print(each_item)
print(f"Total money spend: {total_money_spent:.2f}")

