
alien_0 ={'X_position':0, 'Y_position':25,'speed':'medium'}
print("original X_Postion: "+str(alien_0['X_position']))
alien_0['speed'] = 'fast'
# move the alien to the right
# determine how far to mvoe the alien based on its speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this alien must be fast
    x_increment = 3
# the new posistion is the old position plus x increment
alien_0['X_position'] = alien_0['X_position'] + x_increment

print("New X_position: " + str(alien_0['X_position']))