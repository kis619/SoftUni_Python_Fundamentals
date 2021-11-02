import re
pattern = r"@#+[A-Z][a-zA-Z\d]{4,}[A-Z]@#+" # доуточнение

n = int(input())
for _ in range(n):
    barcode = re.findall(pattern, input())

    if barcode:
        barcode = str(barcode)
        product_group = ""
        for each_char in barcode:

            if each_char.isdigit():
                product_group += each_char

        if product_group == "":
            product_group = "00"

        print(f"Product group: {product_group}")

    else:
        print("Invalid barcode")

