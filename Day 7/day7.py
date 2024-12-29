import random

words_list = ["Apple", "Welcome", "Hello"]

word = words_list[random.randint(0, len(words_list))]

print(word)

user_input = input("Please write a letter: ").lower()

for letter in word:
    if user_input == letter.lower():
        print("Right")
    else:
        print("Wrong")
