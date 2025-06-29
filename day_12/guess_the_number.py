# Моя полностью рабочая версия

# import random

# def thinking_number():
#     '''function takes a random number from 1 to 100 for guessing game'''
#     print("I'm thinking of a number between 1 and 100.")
#     return random.randint(1, 100)

# def tries_amount():
#     '''setting the diffuculty and tryes remaining'''
#     difficulty = input("Set the difficulty: 'easy' or 'hard': ").lower()
#     if difficulty == "easy":
#         return 10
#     elif difficulty == "hard":
#         return 5
#     else:
#         print("There is only 2 options!")
#         return tries_amount()

# def guessing_game():
#     number = thinking_number()
#     attempts = tries_amount()
#     guess = 0
#     while True:
#         if attempts > 0:
#             print(f"You have {attempts} attempts remaining to guess the number.")
#             guess = int(input("Make a guess: "))
#             if guess != number:
#                 if guess > number:
#                     print("Too high.")
#                 else:
#                     print("Too low.")
#             else:
#                 print(f"You got it! The answer was {number}.")
#                 break
#             attempts -=1
#         else:
#             print("You've run out of guesses. LOSE")
#             break

# guessing_game()




# джепетто причесал:



import random

def generate_secret_number():
    """Returns a random number between 1 and 100."""
    # ❗ Переименовал функцию thinking_number → generate_secret_number — более понятное название
    print("I'm thinking of a number between 1 and 100.")
    return random.randint(1, 100)

def get_attempts():
    """Asks user for difficulty level and returns number of attempts."""
    # ❗ Переименовал tryes_ammount → get_attempts — правильное написание и читаемость
    # ❗ Вместо if/elif/else использован словарь levels — проще и масштабируемо
    levels = {"easy": 10, "hard": 5}
    while True:  # ❗ Вместо рекурсии использован цикл while — надёжнее
        difficulty = input("Choose difficulty ('easy' or 'hard'): ").lower()
        if difficulty in levels:
            return levels[difficulty]
        print("Invalid choice. Please enter 'easy' or 'hard'.")

def guessing_game():
    number = generate_secret_number()
    attempts = get_attempts()

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            # ❗ Добавлена обработка неверного ввода — предотвращает падение при вводе текста
            print("Invalid input! Please enter a number.")
            continue

        if guess == number:
            # ❗ Проверку на победу перенёс первой — чтобы логика была: «если угадал — выход сразу»
            print(f"You got it! The answer was {number}.")
            return
        elif guess > number:
            print("Too high.")
        else:
            print("Too low.")

        attempts -= 1

    # ❗ Добавлен вывод задуманного числа при проигрыше — чтобы пользователь узнал правильный ответ
    print(f"You've run out of guesses. You lose. The correct number was {number}.")

guessing_game()
