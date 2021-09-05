number = int(input())
is_prime = True
for i in range(2, number):
    check = number % i
    if check == 0:
        is_prime = False
        break

if is_prime:
    print("True")
else:
    print("False")
