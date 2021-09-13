elements = [el.lower() for el in input().split()]
to_be_printed = []
for el in elements:
    if elements.count(el) % 2 == 1:
        if el not in to_be_printed:
            to_be_printed.append(el)

print(" ".join(to_be_printed))