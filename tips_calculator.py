print("Welcome to the tips calculator!")

bill = round(float(input("Whats the bill ammount?\n")), 2)
tip_percent = int(input("Whats the tips percent: 10, 12 or 15?\n"))
persons = int(input("How many persons?\n"))

ammount_per_person = round(bill * (tip_percent / 100 + 1) / persons, 2)

print(f"You should pay: {ammount_per_person}$")
