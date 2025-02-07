from art import logo

print(logo)
print("Welcome to the secret auction program.")

buyers = {}

keep_going = True
while keep_going:
    name = input("What is your name?: ")
    money = int(input("What's your bid?: $"))
    buyers[name] = money
    uSure =True
    while uSure:
        another_buyer = input("Are there any other Buyers? Type 'yes' or 'no'.\n")
        if another_buyer.lower() == "no":
            keep_going = False
            uSure = False
        elif another_buyer.lower() == "yes":
            uSure = False
            print("\n" * 100)
        else:
            uSure = True
            print("Please enter a valid input")
