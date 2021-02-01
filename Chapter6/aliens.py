# alien_0 = {'color':'Yellow','points':5}
# alien_1 = {'color':'Red','points':10}
# alien_2 = {'color':'Blue','points':15}

# aliens = [alien_0,alien_1,alien_2]
# for alien in aliens:
#     print(alien)

aliens =[]

for alien_num in range(30):
    new_alien = {'color':'yellow','points':5,'speed':'medium'}
    aliens.append(new_alien)

for alien in aliens[:4]:
    if alien['color'] == 'yellow':
        alien['color'] = 'green' 
        alien['points'] = 20 
        alien['speed'] = 'fast'
    #not sure how this code works since the above code does the same thing how this code will run 
    elif alien['color'] == 'yellow': 
        alien['color'] = 'red'
        alien['points'] = 10
        alien['speed'] = 'slow'    

for alien in aliens[:10]:
    print(alien)
print("....")

print("total number of aliens created is "+ str(len(aliens)))

