############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   https://appbrewery.github.io/python-day11-demo/

import random


def set_card():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	return random.choice(cards)


def add_card_player():
	while sum(score["player"]) < 21:
		card = set_card()
		if input(f'У вас на руках {score["player"]} или {sum(score["player"])}.\nЖелаете добавить карту? y/n: ').lower() == "y":
			if sum(score["player"]) > 10 and card == 11:
				score["player"].append(1)
			else:
				score["player"].append(card)
		else:
			return


def add_card_dealer():
	print(f'Первая карта диллера: {score["dealer"][0]}')
	while sum(score["dealer"]) < 17:
		card = set_card()
		if sum(score["dealer"]) > 10 and card == 11:
			score["dealer"].append(1)
		else:
			score["dealer"].append(card)


def winner_is():
	print(f'У диллера на руках: {score["dealer"]} или {sum(score["dealer"])}\nУ игрока: {score["player"]} или {sum(score["player"])}.')
	if sum(score["dealer"]) == sum(score["player"]) or sum(score["dealer"]) > 21 and sum(score["player"]) > 21:
		print("Ничья!")
	else:
		if 21 >= sum(score["player"]) > sum(score["dealer"]) or sum(score["dealer"]) > 21:
			print("Вы победили!")
		elif 21 >= sum(score["dealer"]) > sum(score["player"]) or sum(score["player"]) > 21:
			print("Вы проиграли!")

score = {
	"dealer": [set_card(), set_card()],
	"player": [set_card(), set_card()],
}

print("\nЭТО - ПОЛНОЕ ДЕРЬМО, НЕСООТВЕТСТВУЮЩЕЕ ЗАДАЧЕ.\n")
add_card_dealer()
add_card_player()
winner_is()
