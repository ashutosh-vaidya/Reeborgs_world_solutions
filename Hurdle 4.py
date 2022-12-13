#There is no turn_right() function available, however we have turn_left()
# 3 times turn_left makes turn_right
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
#Here hurdle is of variable length so we need to modify the jump()
def jump():
    #first we will turn left and then check if there is wall on right
    #till wall on right is true move by one step
    turn_left()    
    while wall_on_right():
        move()
    #once there is no wall on right thenstart moving up or down
    turn_right()
    move()
    turn_right()
    #until the front is clear we will move one step forward
    while front_is_clear():
        move()
    #finally we will turn left
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
