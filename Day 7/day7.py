import random

words_list = ["apple", "welcome", "hello"]

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
 ========

''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
 ========
''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
 ========
''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
 ========
''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
 ========
''','''
  +---+
  |   |
  O   |
      |
      |
      |
 ========
''','''
  +---+
  |   |
      |
      |
      |
      |
 ========
'''
]
# word = words_list[random.randint(0, len(words_list))]
word = random.choice(words_list)


print(word)

under_score = ""
for blanks in range(len(word)):
    under_score += "_"
print(under_score)

game_over = True
correct_word = []
i = ""

lives = 6

while game_over != False:

    guesses = ""
    user_input = input("Please write a letter: ").lower()
    for letter in word:
        if user_input == letter:
            guesses += letter
            correct_word.append(user_input)
            i += user_input
            #print("Right")
        elif letter in i: # we can use correct_word list in the place of i and both r the same
            guesses += letter
        else:
            guesses += "_"
            #print("Wrong")

    if user_input not in word:
        lives -=1
    print(stages[lives])
    print(guesses)

    if "_" not in guesses:
        print("You Win!")
        game_over = False
    elif lives == 0:
        print("You Loose!")
        game_over = False
    
