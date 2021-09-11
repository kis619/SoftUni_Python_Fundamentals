list_string = input().split(", ")
money = []
for each_element in list_string:
    money.append(int(each_element))

beggars = int(input())

new_list = []
beggars_having_received_money = 0
while len(money) > 0:
    for each_beggar in range(beggars):
        if len(new_list) < beggars:
            new_list.append(money[0])
            money.pop(0)
            beggars_having_received_money += 1
        else:
            new_list[each_beggar] += money[0]
            money.pop(0)
        if len(money) == 0:
            if beggars - beggars_having_received_money > 0:
                for each_beggar in range(beggars - beggars_having_received_money):
                    new_list.append(0)
            break
print(new_list)