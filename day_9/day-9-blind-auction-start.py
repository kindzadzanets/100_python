
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
	print(f"Победителем аукциона становится {winner} со ставкой {top_bid}$!!!")
	return winner, top_bid


def one_more_bid():
	while True:
		answer = input("Есть ли ещё желающие?\nда\нет: ").lower()
		if answer == "да":
			add_bid()
		else:
			break
	winner_is()

add_bid()
one_more_bid()
