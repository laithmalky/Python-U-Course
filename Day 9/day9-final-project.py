from art import logo

print(logo)
print("Welcome to the secret auction program.")

buyers = {}

def find_buyer(bname, bmoney):
    highest_money = 0
    highest_buyer = ""
    for word in buyers:
        if buyers[word] > highest_money:
            highest_money = buyers[word]
            highest_buyer = word
    print(f"The winner is {highest_buyer} with a payment of ${highest_money}")


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
            print("\n" * 100)
            find_buyer(name, money)
        elif another_buyer.lower() == "yes":
            uSure = False
            print("\n" * 100)
        else:
            uSure = True
            print("\n" * 100)
            print("Please enter a valid input")
