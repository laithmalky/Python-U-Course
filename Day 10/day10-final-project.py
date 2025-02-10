from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

values = { 
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide,
    }

# print(values["*"](4,8))

first_input = float(input("Enter the first number: "))

in_go = 'y'
while in_go == 'y':
    for key in values:
        print(key)
    
    calculat = input("Pick an operation from the line above: ")

    for word in range(0, 101):
        if calculat in values:
            break
        else:
            print("Invalid operation")
            calculat = input("Please pick the right operation from the line above: ")

    second_input = float(input("Enter the next number: "))
    
    calculation = values[calculat]
    answer = calculation(first_input, second_input)
    
    print(f"{first_input} {calculat} {second_input} = {answer}")
    
    
    for word in range(0,101):
        
        in_go_check = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if in_go_check == 'y':
            first_input = answer
            break

        elif in_go_check == 'n':
            in_go = 'n'
            print("Goodbye")
            break
    
        else:
            print("Invalid input")
