print("Hi! Welcome to Crazy Park!")

height = int(input("What is your height cm? "))

if height >= 120:
    age = int(input("How old are you, my friend? "))
    price = 0
    if age < 12:
        price += 5
    elif age < 18:
        price += 7
    elif age >= 45 and age <= 55:
        print("Ride for free, old pice of shit!")
    else:
        price += 12

    photo = input("Wold you like to have a photo of your trip? (Y/N) ").upper()
    if photo == "Y":
        price += 3

    print(f"Your total bill is: {price}$")

else:
    print("Sorry, but you can't ride today... I wish you will drink much more milk and will come back after!")