import random

words_list = ["Apple", "Welcome", "Hello"]

# word = words_list[random.randint(0, len(words_list))]
word = random.choice(words_list)


print(word)

under_score = ""
for blanks in range(len(word)):
    under_score += "_"
print(under_score)

user_input = input("Please write a letter: ").lower()

guesses = ""
for letter in word:
    if user_input == letter.lower():
        guesses += letter
        #print("Right")
    else:
        guesses += "_"
        #print("Wrong")
print(guesses)
