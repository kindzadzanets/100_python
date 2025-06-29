import random


def deal_card():
	"""возвращает случайную карту из колоды"""
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	return random.choice(cards)


def calculate_score(cards):
	"""функция принимает нужный список карт в аргументе и вычисляет сумму очков"""
	if sum(cards) == 21 and len(cards) == 2:
		return 0
	if 11 in cards and sum(cards) > 21:
		cards[cards.index(11)] = 1
	return sum(cards)


def compair_scores(user_score, dealer_score):
	"""сравнивает счет игрока и дилера и определяет победителя"""
	if user_score == dealer_score:
		return "\nНичья! 🫥"
	elif dealer_score == 0:
		return "\nПроиграл! У диллера: Очко! 💩"
	elif user_score == 0:
		return "\nПобеда! У тебя: Очко! 😎"
	elif user_score > 21:
		return "\nПроиграл! У тебя: Перебор! 🤡"
	elif dealer_score > 21:
		return "\nПобеда! У диллера: Перебор! 💋"
	elif user_score > dealer_score:
		return "\nПобеда! Утебя: Больше! 🍆"
	else:
		return "\nПроиграл! У тебя: меньше! 🤏🏻"


def play_game():
	user_cards = []
	dealer_cards = []
	is_game_over = False


	for _ in range(2):
		user_cards.append(deal_card())
		dealer_cards.append(deal_card())


	while not is_game_over:
		user_score = calculate_score(user_cards)
		dealer_score = calculate_score(dealer_cards)
		print(f"\n  У тебя: {user_cards} или {user_score}.")
		print(f"  Первая карта диллера: {dealer_cards[0]}.")
		if user_score == 0 or dealer_score == 0 or user_score > 21:
			is_game_over = True
		else:
			user_should_deal = input("Желаете добавить карту? y/n: ").lower()
			if user_should_deal == "y":
				user_cards.append(deal_card())
			else:
				is_game_over = True

	while 0 < dealer_score < 17:
		dealer_cards.append(deal_card())
		dealer_score = calculate_score(dealer_cards)

	print(f"\n  В итоге у тебя: {user_cards} или {user_score}.")
	print(f"  У диллера: {dealer_cards} или {dealer_score}.")
	print(compair_scores(user_score, dealer_score))


while input("\n  Хочешь сыграть Очко? y/n: ").lower() == "y":
	play_game()