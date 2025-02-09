
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

print(format_name(first_name, last_name))


# efficient way

def format_name(fname, lname):
    # f_name = fname.capitalize()
    # l_name = lname.capitalize()
    # return f_name + " " + l_name
    return fname.capitalize() + " " + lname.capitalize()

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(format_name(first_name, last_name))
