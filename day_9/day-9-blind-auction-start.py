import pyautogui
import time

bidders = {}

def add_bid():
	print("Добро пожаловать на секретный аукцион!\n")
	name = input("Как вас зовут?\n").capitalize()
	amount = int(input("Каков размер вашей ставки $?\n"))
	bidders[name] = amount
	print(bidders)

def winner_is():
	top_bid = 0
	winner = None
	for key in bidders:
		if bidders[key] > top_bid:
			top_bid = bidders[key]
			winner = key
	return winner, top_bid
	print(f"Победителем аукциона становится {winner} со ставкой {top_bid}$!!!")





def one_more_bid():
	answer = input("Есть ли ещё желающие?\nда\нет: ").lower()
	while answer == "да":
		add_bid()
		one_more_bid()
	winner_is()

add_bid()
one_more_bid()