import random

words_list = ["Apple", "Welcome", "Hello"]

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

while game_over != False:

    guesses = ""
    user_input = input("Please write a letter: ").lower()
    for letter in word:
        if user_input == letter.lower():
            guesses += letter
            correct_word.append(user_input)
            i += user_input
            #print("Right")
        elif letter in i:
            guesses += letter
        else:
            guesses += "_"
            #print("Wrong")
    print(guesses)

    if "_" not in guesses:
        print("You Win!")
        game_over = False
