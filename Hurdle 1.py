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
    
#Since we have 6 hurdles in total we can use the for loop and call jump 6 times.
for i in range(6):
    jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
