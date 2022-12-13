#There is no turn_right() function available, however we have turn_left()
# 3 times turn_left makes turn_right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#The jump function is the steps required to pass one hurdle    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
#Since no of hurdles are going to be random we need to check if Reeborg is at the goal or not
#If not at goal then perform jump. We can use while loop to achieve this
while not at_goal():
    jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
