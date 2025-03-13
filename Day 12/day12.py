enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")


# Local scope: A variable created inside a function is available inside that function.

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength) # This will throw an error as potion_strength is not available outside the function.


# Global scope: A variable created outside a function is available inside the function.
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)
    print(potion_strength)

drink_potion()
print(player_health)
# print(potion_strength) # This will throw an error as potion_strength is not available outside the function.