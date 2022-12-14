def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def move_3_steps():
    for i in range(3):
        move()
        
def make_U_turn():
    if not at_goal():
        turn_right()
        move()
        turn_right()    
    
def move_in_Lshape():
    move_3_steps()
    turn_left()
    move_3_steps()
    
while not at_goal():
    move_in_Lshape()
    make_U_turn()
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
