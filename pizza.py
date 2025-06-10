print("Welcome to python-pizza!")

size = input("Choose the size: S, M or L: ")[0].upper()
pepperoni = input("Would you like to add pepperoni? Y or N: ")[0].upper()
extra_cheese = input("Do you want an extra cheese? Y or N: ")[0].upper()
price = 0

if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25
else:
    print("Please choose one of proposed!")

if pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if extra_cheese == "Y":
    price += 1

print(f"Your order ammount is: {price}$")