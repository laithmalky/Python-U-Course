from random import choice
from art_list import stages, art
from words_list import words_listing
# using from better than using import because we don't have to use the module name before the function or variable name

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
def under_score_fun(word):
    under_score = ""
    for blanks in range(len(word)):
        under_score += "_"
    return under_score

def prints(lives, guesses):
    print(stages[lives])
    print(guesses)


print(art)
print("Welcome to the hangman game!")

word = choice(words_listing)

#print(word)

print(f'{under_score_fun(word)}\n')

# under_score = ""
# for blanks in range(len(word)):
#     under_score += "_"
# print(under_score)

game_over = True
correct_word_list = []
correct_word = ""

lives = 6
used_before = False
not_in_word = False

while game_over != False:

    guesses = ""
    user_input = input("Please write a letter: ").lower()
    if user_input in correct_word:
        used_before = True

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
        not_in_word = True
        # if lives == 0:
        #     print("You Loose!")
        #     game_over = False
    
    prints(lives, guesses)

    # print(art_list.stages[lives])
    # print(guesses)

    if used_before == True:
        print(f'You used this letter before: {user_input}')
        used_before = False

    if not_in_word == True:
        print(f'This letter is not in the word: {user_input}')
        not_in_word = False

    print(f'********** {lives}/6 LIVES LEFT **********')

    if "_" not in guesses:
        print("********** YOU WIN **********")
        game_over = False
    elif lives == 0:
        print("********** YOU LOST **********")
        game_over = False
