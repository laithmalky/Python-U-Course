from day11_project_art import art
from random import choice

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def game():
    game_start = input("Do you want to play a game of blackjack? Type 'y' for yes or 'n' for no: ")

    if game_start.lower() == 'y':
        print('\n' * 100)
        print(art)
        print("Welcome to the game of Blackjack!")
        start_game()
    elif game_start.lower() == 'n':
        print("Goodbye!")
    else:
        print("Invalid input! Please try again.")
        game()

def start_game():
    user_cards = [choice(cards), choice(cards)]
    computer_cards = [choice(cards), choice(cards)]

    def calculate_score(cards):
        if 11 in cards and sum(cards) > 21:
            the_sum = sum(cards) - 10
            return the_sum
            
        else:
            return sum(cards)
        
    def compare(user_sum, computer_sum):
        if user_sum == computer_sum:
            print("It's a draw!")
        elif computer_sum == 21:
            print("Computer wins!")
        elif user_sum == 21:
            print("You win!")
        elif user_sum > 21:
            print("You went over. Computer wins!")
        elif computer_sum > 21:
            print("Computer went over. You win!")
        elif user_sum > computer_sum:
            print("You win!")
        else:
            print("Computer wins!")
        

    # num_user_cards = len(user_cards)
    # num_computer_cards = len(computer_cards)
    def sums():
        user_sum = calculate_score(user_cards)
        computer_sum = calculate_score(computer_cards)
        compare(user_sum, computer_sum)
        
    def printing():
        print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")

    while 0 < sum(user_cards) < 21:
        printing()
        user_input = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_input == 'n':
            sums()
            printing()
            break
        elif user_input == 'y' and sum(user_cards) < 21:
            user_cards.append(choice(cards))
        elif user_input == 'y' and sum(user_cards) > 21:
            sums()
            printing()
            break
        else:
            print("Invalid input! Please try again.")

game()
