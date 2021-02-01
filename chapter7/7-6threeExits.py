# age = input("how old are you: ")
# age = int(age)
tickets = 6
opened = True
while opened:
    tickets -= 1
    if tickets == 0:
        print("we are out of tickets")
        break 
    age = input("how old are you: ")
    age = int(age)
    if age == 'quit':
        break
    if age == 99:
        print('you are not allowed to watch this movie')
        opened = False
    if age <= 3:
        print("your ticket is free")
    elif age <= 12:
        print("your ticket will cost $10")
    else:
        print("your ticket will cost $15")

