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


# you can edit the value of a key in the dictionary
empty_dictionary["key"] = "new value"
print(empty_dictionary)

# you can also clear the dictionary
empty_dictionary = {}
print(empty_dictionary)


# we can use for loop 
for word in first_dictionary:
    print(word)
    print(first_dictionary[word])



# First Task

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for grade in student_scores:
    if 91 <= student_scores[grade] <= 100:
        student_grades[grade] = "Outstanding"
    elif 81 <= student_scores[grade] <= 90:
        student_grades[grade] = "Exceeds Expectations"
    elif 71 <= student_scores[grade] <= 80:
        student_grades[grade] = "Acceptable"
    elif student_scores[grade] <= 70:
        student_grades[grade] = "Fail"

print(student_grades)


# Simple way 
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# How to get inside the list that inside the dictionary
print(travel_log["France"])
print(travel_log["France"][1])
