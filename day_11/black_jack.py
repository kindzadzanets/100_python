import random

def set_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


player_cards = [set_card()]
dealer_cards = [set_card()]

if player_cards[0] == 11:
    player_cards.append(1)
else:
    player_cards.append(set_card())

if dealer_cards[0] == 11:
    dealer_cards.append(1)
else:
    dealer_cards.append(set_card())


def adding_cards():
    while True:
        if sum(player_cards) == 21:
            print("Blackjack! You WIN!")
            break

        if sum(player_cards) < 21:
            print(f"You have {player_cards} = {sum(player_cards)}, dealer's first card is {dealer_cards[0]}")
            add_card_player = input("Would you like to add a card? 'y' or 'n': \n").lower()

            if sum(dealer_cards) < 17:
                card = set_card()
                if card == 11 and sum(dealer_cards) > 10:
                    dealer_cards.append(1)
                else:
                    dealer_cards.append(card)

            if add_card_player == "y":
                card = set_card()
                if card == 11 and sum(player_cards) > 10:
                    player_cards.append(1)
                else:
                    player_cards.append(card)
            elif add_card_player == "n":
                winner()
                break
        else:
            winner()
            break


def winner():
    print(f"\nYour hand: {player_cards} = {sum(player_cards)}")
    print(f"Dealer's hand: {dealer_cards} = {sum(dealer_cards)}")

    if sum(player_cards) > 21:
        print("You LOOSE! (You went over 21)")
    elif sum(dealer_cards) > 21:
        print("You WIN! (Dealer went over 21)")
    elif sum(player_cards) == sum(dealer_cards):
        print("It's a DRAW!")
    elif sum(player_cards) > sum(dealer_cards):
        print("You WIN!")
    else:
        print("You LOOSE!")


adding_cards()