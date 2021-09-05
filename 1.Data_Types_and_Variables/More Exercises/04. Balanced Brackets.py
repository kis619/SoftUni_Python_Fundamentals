n = int(input())
is_balanced = True
bracket_counter = 0
for each_entry in range(n):
    if is_balanced == False:
        break
    entry = input()
    if entry == "(":
        bracket_counter += 1
        if bracket_counter > 1:
            is_balanced = False
    elif entry == ")":
        if bracket_counter == 0:
            is_balanced = False
        elif bracket_counter == 1:
            bracket_counter = 0
            is_balanced = True
        else:
            is_balanced = False

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
