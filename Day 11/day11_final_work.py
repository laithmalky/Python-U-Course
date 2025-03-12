import random
from day11_project_art import art

def deal_cards():
    # return random card from the list of cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    # take the list of the cards and return the calculated score of the cards
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards) 


user_cards = []
computer_cards = []
is_game_over = False


for i in range(2):
    # new_card = deal_cards()
    # user_cards.append(new_card)
    # computer_cards.append(new_card)
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())
    
    
while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")


    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal.lower() == 'y':
            user_cards.append(deal_cards())
        else:
            is_game_over = True
