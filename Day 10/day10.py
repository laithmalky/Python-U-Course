
import calendar

# Make the first letter of the first name and last name capital and the rest of the letters in lower case.

# basic way
def format_name(fname, lname):
    f_name= ""
    l_name = ""
    for i in range(0, len(fname)):
        if i == 0 :
            f_name += fname[i].upper()
        else:
            f_name += fname[i].lower()

    for i in range(0, len(lname)):
        if i == 0 :
            l_name += lname[i].upper()
        else:
            l_name += lname[i].lower()
    
    return f_name + " " + l_name
            


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(format_name(fname = first_name, lname = last_name))


# efficient way

def format_name(fname, lname):
    # f_name = fname.capitalize()
    # l_name = lname.capitalize()
    # return f_name + " " + l_name
    return fname.capitalize() + " " + lname.capitalize()

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(format_name(first_name, last_name))


# for the sentence
def format_sentence(sentences):
    return sentence.title()

sentence = input("Enter a sentence: ")
print(format_sentence(sentence))


# use multiple functions
def function1(word):
    return word + word

def function2(word):
    return word.title()

input_word = input("Enter a word: ")
print(function2(function1(input_word)))

# use multiple return
def format_name(fname, lname):
    if fname == "" or lname == "":
        return "You didn't provide valid inputs."
    # f_name = fname.capitalize()
    # l_name = lname.capitalize()
    # return f_name + " " + l_name
    return f"Result: {fname.title()} {lname.title()}"

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(format_name(first_name, last_name))


# first example


'''
def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    is_right = False
    if year % 4 == 0:
        is_right = True
    if year % 100 == 0:
        is_right = False
    if year % 400 == 0:
        is_right = True
    
    return is_right
'''

def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    return calendar.isleap(year)
    

print(is_leap_year(1989))

