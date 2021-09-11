list_string = input().split(", ")
beggars = int(input())
money = []
for each_element in list_string:
    money.append(int(each_element))

new_list = [0] * beggars
for i in range(len(money)):
    new_list[i % beggars] += money[i]

print(new_list)