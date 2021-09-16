my_text = input()
position = 0
to_be_replaced = ""
while True:

    if position == len(my_text) - 1:
        if my_text[position - 1] == my_text[position]:
            to_be_replaced += my_text[position]
            my_text = my_text.replace(to_be_replaced, my_text[position], 1)

        break

    if my_text[position] == my_text[position + 1]:
        to_be_replaced += my_text[position]

    elif not my_text[position] == my_text[position + 1]:
        to_be_replaced += my_text[position - 1]
        my_text = my_text.replace(to_be_replaced, my_text[position - 1], 1)
        position = position + 1 - len(to_be_replaced)
        to_be_replaced = ""
    position += 1


print(my_text)