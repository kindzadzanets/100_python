# версия джепетто (с комментариями):

from data import coffee_types, coins, resources
import copy  # нужен, чтобы не портить исходный resources


def action_request():
    """Запрашивает команду у пользователя и возвращает её в виде строки, проверяя корректность"""
    command = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while command not in ("espresso", "latte", "cappuccino", "off", "report", "add"):
        print("Unknown instruction!")
        command = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return command


def fill_supplies(balance):
    """Заполняет ресурсы до максимума. Просто устанавливает значения вручную"""
    balance["water"] = 200
    balance["milk"] = 300
    balance["coffee"] = 70
    return balance


def resources_checker(which_coffee, balance, recipe):
    """
    Принимает:
    - which_coffee: строка — название выбранного кофе (например, "latte").
    - balance: словарь с текущим запасом ингредиентов (например: {"water": 300, "milk": 200, "coffee": 100}).
    - recipe: список словарей, каждый из которых — это рецепт одного вида кофе с его ингредиентами и ценой.

    Возвращает:
    - True, если всех нужных ингредиентов достаточно;
    - False, если чего-то не хватает или кофе не найден.
    """

    # Проходим по каждому рецепту в списке recipe
    for coffee in recipe:
        # Проверяем, совпадает ли название рецепта с выбранным кофе
        if coffee["name"] == which_coffee:
            # Если найден нужный кофе, проходим по всем парам "ингредиент — количество" в рецепте
            for ingredient, amount in coffee.items():
                # Пропускаем ключи "name" и "price", так как это не ингредиенты
                if ingredient == "name" or ingredient == "price":
                    continue  # continue означает "пропустить эту итерацию и перейти к следующей"

                # Получаем текущее количество ингредиента на складе (в балансе)
                # Если нужный ингредиент отсутствует — считаем, что его 0
                if balance.get(ingredient, 0) < amount:
                    # Если ингредиента меньше, чем нужно по рецепту — возвращаем False
                    return False

            # Если все нужные ингредиенты есть в достатке — возвращаем True
            return True

    # Если ни один рецепт не подошёл (не нашли кофе с таким названием) — возвращаем False
    return False


def coffee_price(which_coffee, recipe):
    """Выводит цену выбранного кофе и возвращает её"""
    for coffee in recipe:
        if coffee["name"] == which_coffee:
            price = coffee["price"]
            print(f"{which_coffee.capitalize()} costs: ${price}")
            return price
    return 0  # на всякий случай, если кофе не найден (не должен сработать при правильной логике)


def coin_collector(coin_types, price):
    """
    Принимает монеты от пользователя и возвращает True, если достаточно денег, иначе False.
    """
    amount = 0.0
    for key, value in coin_types.items():
        inserted = float(input(f"How many {key} - (${value}) would you like to insert?: "))
        amount += inserted * value
    amount = round(amount, 2)  # округляем один раз после всех сложений

    print(f"Total inserted: ${amount}")
    if amount >= price:
        if amount > price:
            change = round(amount - price, 2)
            print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def remains_recount(which_coffee, recipe, balance):
    """Списывает ингредиенты и добавляет деньги после приготовления кофе"""
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
    """Выводит текущие остатки ингредиентов с единицами измерения"""
    print("Current balance is:")
    units = {"water": "ml", "milk": "ml", "coffee": "gr", "money": "$"}
    for key, value in balance.items():
        unit = units.get(key, "")
        print(f"{key.capitalize():<10}: {value}{unit}")
    # return здесь не нужен


def coffee_machine():
    """Основной цикл кофемашины"""
    off = False
    remains = copy.deepcopy(resources)  # создаём копию, чтобы не испортить оригинал из модуля
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
            enough_resources = resources_checker(user_choice, remains, coffee_types)

            if not enough_resources:
                print("There is not enough ingredients. Please call support and use 'add'.")
                continue  # возвращаемся в начало цикла

            # Предлагаем оплатить
            while True:
                paid = coin_collector(coins, price)
                if paid:
                    remains_recount(user_choice, coffee_types, remains)
                    print(f"Here is your {user_choice.capitalize()}. Enjoy!")
                    break  # переходим к следующей итерации (новый заказ)
                else:
                    try_again = input("Would you like to try pay again? y or n: ").lower()
                    if try_again != "y":
                        break  # человек отказался — возвращаемся к выбору команды

coffee_machine()