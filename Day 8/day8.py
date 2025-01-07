# Description: Functions in Python 
def greet():
    print("Hello")
    print("Good Morning")
    print("Good Night")

greet()


# Function with parameters and arguments
def greet_name(name):
    print(f'Hello, {name}')
    print(f'Good Morning {name}')
    print(f'Good Night {name}')

greet_name('John')

# Function with more than 1 input
def greet_with(name, location):
    print(f'Hello, {name}')
    print(f'Good Morning {name} from {location}')
    print(f'Good Night {name} from {location}')

greet_with('John', 'New York')
#greet_with('New York', 'John') # Order of arguments matters "Positional Arguments"
