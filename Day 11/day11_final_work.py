import random
from day11_project_art import art

def deal_cards():
    # return random card from the list of cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []

for i in range(2):
    # new_card = deal_cards()
    # user_cards.append(new_card)
    # computer_cards.append(new_card)
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())
    