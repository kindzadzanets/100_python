Import Logo and List of dicts
Show logo
create a function to show first random pair of elements and next pair like: first_el = prev_second_el, second_el = random
create compairing function which result will move fourward or end the game and score counting

import random
from logos import logo_dict
from capitals_list import capitals

logo = logo_dict["game_logo"]
versus = logo_dict["vs_logo"]



# def show_pair():
score = 0
a = random.choice(capitals)
while True:
    b = random.choice(capitals)
    while b == a:
        b = random.choice(capitals)
    print(f"Compare A: {a["name"]}, a capital of {a["country"]}, {a["continent"]}.")
    print(versus)
    print(f"Against B: {b["name"]}, a capital of {b["country"]}, {b["continent"]}.")
    choiсe = input("Which population is higher? A or B:  ").lower()
    if choiсe in ("a", "b"):
        if choiсe == "a" and a["population"] > b["population"] or choiсe == "b" and b["population"] > a["population"]:
            a = b
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            if a["population"] > b["population"]:
                print(f"No, population of {a["name"]}: {a["population"]} is higher then {b["name"]}: {b["population"]}")
            else:
                print(f"No, population of {b["name"]}: {b["population"]} is higher then {a["name"]}: {a["population"]}")
            print(f"YOU LOSE! Final score: {score}")
            break
    else:
        print(f"You've added a wrong value, try again please.")
        break


# версия джепетто:

# import random
# from logos import logo_dict
# from capitals_list import capitals


# def print_logo():
#     """Печатает логотип игры."""
#     print(logo_dict["game_logo"])


# def get_random_city(exclude=None):
#     """Возвращает случайный город, не равный exclude (если указан)."""
#     city = random.choice(capitals)
#     while exclude and city == exclude:
#         city = random.choice(capitals)
#     return city


# def format_city_info(label, city):
#     """Возвращает отформатированную строку для одного города."""
#     return f"{label}: {city['name']}, capital of {city['country']}, {city['continent']}."


# def compare_populations(a, b, user_choice):
#     """Возвращает True, если пользователь угадал правильно, иначе False."""
#     if user_choice == 'a':
#         return a["population"] > b["population"]
#     elif user_choice == 'b':
#         return b["population"] > a["population"]
#     return False


# def print_result(correct, a, b):
#     """Печатает результат ответа."""
#     if correct:
#         print("You're right!")
#     else:
#         if a["population"] > b["population"]:
#             print(f"No, population of {a['name']}: {a['population']:,} "
#                   f"is higher than {b['name']}: {b['population']:,}")
#         else:
#             print(f"No, population of {b['name']}: {b['population']:,} "
#                   f"is higher than {a['name']}: {a['population']:,}")


# def play_game():
#     """Основная игровая логика."""
#     print_logo()
#     score = 0
#     a = get_random_city()

#     while True:
#         b = get_random_city(exclude=a)

#         print(format_city_info("Compare A", a))
#         print(logo_dict["vs_logo"])
#         print(format_city_info("Against B", b))

#         choice = input("Which population is higher? Type 'A' or 'B': ").strip().lower()

#         if choice not in ["a", "b"]:
#             print("Invalid input. Please type 'A' or 'B'.\n")
#             continue

#         is_correct = compare_populations(a, b, choice)
#         print_result(is_correct, a, b)

#         if is_correct:
#             score += 1
#             a = b  # Победитель переходит в следующий раунд
#             print(f"Current score: {score}\n")
#         else:
#             print(f"\nGAME OVER! Final score: {score}")
#             break


# # Запуск
# if __name__ == "__main__":
#     play_game()






