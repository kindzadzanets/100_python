from data import coffee_types, coins, resources


def action_request():
    """returns only the operation name to do and validates it"""
    command = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while command not in ("espresso", "latte", "cappuccino", "off", "report", "add"):
        print("Unknown instruction!")
        command = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return command


def fill_supplies(balance):
    """takes the resourses dict and fills an ingridients for coffee - just makes the full values every time"""
    balance["water"] = 200
    balance["milk"] = 300
    balance["coffee"] = 70
    return balance


def resources_checker(which_coffee, balance, recipe):
    """takes a name of coffee_type, current remains and recipe of coffe and cheks is it enoght ingridients on balance. return True/False"""
    if which_coffee == recipe[0]["name"]:
        return (
            balance["water"] >= recipe[0]["water"]
            and balance["coffee"] >= recipe[0]["coffee"]
        )
    elif which_coffee == recipe[1]["name"]:
        return (
            balance["water"] >= recipe[1]["water"]
            and balance["coffee"] >= recipe[1]["coffee"]
            and balance["milk"] >= recipe[1]["milk"]
        )
    elif which_coffee == recipe[2]["name"]:
        return (
            balance["water"] >= recipe[2]["water"]
            and balance["coffee"] >= recipe[2]["coffee"]
            and balance["milk"] >= recipe[2]["milk"]
        )
    else:
        return False


def coffee_price(which_coffee, recipe):
    """takes ordered coffee name and all coffee types dict,
    prints price and returns the price amount."""
    price = 0
    for coffee in recipe:
        if coffee["name"] == which_coffee:
            price = coffee["price"]
    print(f"{which_coffee.capitalize()} costs: ${price}")
    return price


def coin_collector(coin_types, price):
    """
    Takes coin types dict and price amount, counts how many coins were inserted,
    and returns True if enough was paid, otherwise False.
    """
    amount = 0.0
    for key, value in coin_types.items():
        amount += (
            float(input(f"How many {key} - (${value}) would you like to insert?: "))
            * value
        )
        amount = round(amount, 2)
        print(f"Now it's ${amount}")
    if amount >= price:
        if amount > price:
            change = round(amount - price, 2)
            print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def remains_recount(which_coffee, recipe, balance):
    """takes chossed coffee type, recipes dict and current remains
    and returns new remains minus portion of choosed coffee"""
    for coffee in recipe:
        if coffee["name"] == which_coffee:
            for ingredient, amount in coffee.items():
                if ingredient == "name":
                    continue
                if ingredient == "price":
                    balance["money"] += amount
                else:
                    balance[ingredient] -= amount
            return balance
    raise ValueError(f"Not enough ingredients to make {which_coffee}")


def show_report(balance):
    """takes current remains and print it in suitable format"""
    print("Current balance is:")
    for key, value in balance.items():
        if key in ("water", "milk"):
            print(f"{key.capitalize():<10}: {value}ml")
        elif key == "coffee":
            print(f"{key.capitalize():<10}: {value}gr")
        elif key == "money":
            print(f"{key.capitalize():<10}: ${value}")
        else:
            print(f"{key.capitalize():<10}: {value}")
    return


def coffee_machine():
    off = False
    remains = resources
    fill_supplies(remains)
    while not off:
        user_choice = action_request()
        if user_choice == "off":
            print("Machine was switched off...")
            off = True
        elif user_choice == "report":
            show_report(remains)
        elif user_choice == "add":
            fill_supplies(remains)
        else:
            price = coffee_price(user_choice, coffee_types)
            is_enought_resources = resources_checker(user_choice, remains, coffee_types)
            if is_enought_resources:
                add_money = "y"
                while add_money == "y":
                    is_enought_money = coin_collector(coins, price)
                    if is_enought_money:
                        remains_recount(user_choice, coffee_types, remains)
                        print(f"Here is your {user_choice.capitalize()}. Enjoy!")
                        add_money = 'n'
                    else:
                        add_money = input(
                            f"Would you like to try pay again? y or n: "
                        ).lower()
            else:
                print("There is not enought ingredients. Please call to our support and ask to 'add'! ")

coffee_machine()
