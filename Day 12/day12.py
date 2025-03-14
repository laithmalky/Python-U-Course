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


def game():
    def drink_potion_T2():
        potion_strength = 2
        print(player_health)
        print(potion_strength)
    
    drink_potion_T2()


# drink_potion_T2() # This will throw an error as drink_potion_T2 is not available outside the function.
game()
print(player_health)
# print(potion_strength) # This will throw an error as potion_strength is not available outside the function.



# There is no block scope in Python.

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]

# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy) # This will not throw an error as new_enemy is available outside the if block.


# game_level = 3
game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = ""
    # if game_level bigger than 5 it will throw an error in a print because new_enemy is not defined it needs to be less than 5
    # to get defined.
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy) 

# print(new_enemy) # This will not throw an error as new_enemy is available outside the if block.


# Modifying Global Scope
# Back to the original code
enemies = 1

def increase_enemies():
    enemies += 1
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")
