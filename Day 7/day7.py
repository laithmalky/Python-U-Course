import random
import art_list
import words_list


# words_list = ["apple", "welcome", "hello"]


# stages = [
#     '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
#  ========

# ''','''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
#  ========
# ''','''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
#  ========
# ''','''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
#  ========
# ''','''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
#  ========
# ''','''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
#  ========
# ''','''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
#  ========
# '''
# ]


# word = words_list[random.randint(0, len(words_list))]

print(art_list.art)
print("Welcome to the hangman game")

word = random.choice(words_list.words_listing)

print(word)

under_score = ""
for blanks in range(len(word)):
    under_score += "_"
print(under_score)

game_over = True
correct_word_list = []
correct_word = ""

lives = 6
used_before = False

while game_over != False:

    guesses = ""
    user_input = input("Please write a letter: ").lower()
    if user_input in correct_word:
        used_before = True
        lives -= 1

    for letter in word:
        if user_input == letter:
            guesses += letter
            correct_word_list.append(user_input)
            correct_word += user_input
                #print("Right")

        elif letter in correct_word: # we can use correct_word_list in the place of i and both are the same
            guesses += letter

        else:
            guesses += "_"
            #print("Wrong")


    if user_input not in word:
        lives -= 1
        print(f'This letter is not in the word: {user_input}')
        # if lives == 0:
        #     print("You Loose!")
        #     game_over = False
    

    print(art_list.stages[lives])
    print(guesses)
    if used_before == True:
        print(f'You used this letter before: {user_input}')
        used_before = False


    if "_" not in guesses:
        print("********** You Win **********")
        game_over = False
    elif lives == 0:
        print("********** You Lost **********")
        game_over = False
