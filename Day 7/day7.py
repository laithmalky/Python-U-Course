import random

words_list = ["Apple", "Welcome", "Hello"]

word = words_list[random.randint(0, len(words_list))]

print(word)

user_input = input("Please write a letter: ").lower()

print(user_input)