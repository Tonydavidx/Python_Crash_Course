# age = input("how old are you: ")
# age = int(age)

while True:
    age = input("how old are you: ")
    age = int(age)
    if age <= 3:
        print("your ticket is free")
    elif age <= 12:
        print("your ticket will cost $10")
    else:
        print("your ticket will cost $15")

