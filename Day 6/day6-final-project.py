print("Test")

# robot tasks 

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world3.json&url=user_world%3Aproblem_world3.json

'''

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def moving():
    while wall_in_front():
        if wall_on_right():
            turn_left()
        else:
            turn_right()
    move()
    
'''
'''
while front_is_clear():
    move()
turn_left()
'''
'''

i = 0
while at_goal() == False:
    if right_is_clear() and i < 5:
        turn_right()
        move()
        i += 1
    elif wall_in_front():
        moving()
        i += 1
        if i >12 :
            i = 0
    #elif wall_on_right():
    #    turn_left()
    else:
        move()


'''