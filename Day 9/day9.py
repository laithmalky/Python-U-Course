first_dictionary = {"Bug": "An error in a program that prevents it from running as expected.",
                    "Function": "A piece of code that you can easily call over and over again.",
                    "Loop": "The action of doing something over and over again.",
                    }

# the dictionary is more like the list but it has key value pairs
# the key is the word and the value is the definition of the word
# you can access the value by using the key

print(first_dictionary["Bug"])

first_dictionary[123] = "This is a number"
print(first_dictionary[123])
print(first_dictionary)


# you can create an empty dictionary and add values to it later

empty_dictionary = {}
empty_dictionary["key"] = "value"
print(empty_dictionary)


# you can also clear the dictionary
empty_dictionary = {}
print(empty_dictionary)
