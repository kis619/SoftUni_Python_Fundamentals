first_line = input().split()


first_line_integers = [int(x) for x in first_line]
print(first_line_integers)

print(" * ". join([str(x) for x in first_line_integers]))