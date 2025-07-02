from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
coin_acceptor = MoneyMachine()

def coffee_machine():
    off = False
    while not off:
        choice = input(f"What would you like? {menu.get_items()}: ")
        if choice == "off":
            off = True
            print("The machine is switched off.")
        elif choice == "report":
            coffee_maker.report()
            coin_acceptor.report()
        else:
            coffee = menu.find_drink(choice)
            enought_ingridients = coffee_maker.is_resource_sufficient(coffee)
            if enought_ingridients:
                print(f"Your order: {coffee.name}, price: ${coffee.cost}")
                payment_successful = coin_acceptor.make_payment(coffee.cost)
                if payment_successful:
                    coffee_maker.make_coffee(coffee)
            else:
                print("Call somebody to help")
                    

coffee_machine()