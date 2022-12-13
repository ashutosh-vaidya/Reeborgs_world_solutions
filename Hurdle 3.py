#There is no turn_right() function available, however we have turn_left()
# 3 times turn_left makes turn_right
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
#The jump function is the steps required to pass one hurdle
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
#We do not know number of hurdles and also 
#if there is wall or clear space in front
#We will first check if wall in front, if yes then jump()
#notice that we have removed first move() from the jump
#Instead we will move the reeborg if front is clear
while not at_goal():
    if wall_in_front():
        jump()
    elif front_is_clear():
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
