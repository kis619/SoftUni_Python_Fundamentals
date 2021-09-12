# Write a function which calculates the total price of an order and returns it.
# The function should receive one of the following products: "coffee", "coke", "water" or "snacks", and a quantity of the product.
# The prices for a single piece of each product are:

# •	coffee - 1.50
# •	water - 1.00
# •	coke - 1.40
# •	snacks - 2.00
#
# Print the result formatted to the second decimal place.
def calculate_price(product, quantity):
    """receives a product, whose price is defined,
       receives the quantity of the product,
       returns the calculated price"""
    price = 0
    if product == "coffee":
        price = 1.5
    elif product == "water":
        price = 1
    elif product == "coke":
        price = 1.4
    elif product == "snacks":
        price = 2
    return price * quantity


type_of_product = input()
quantity_of_product = int(input())
total_price = calculate_price(type_of_product, quantity_of_product)
print(f"{total_price:.2f}")