from random import choice
from random import randint
from random import shuffle

seriel_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'f', 'h', 'a', 's', 'r']
shuffle(seriel_number)

ticket = seriel_number[0:4]

print(f"any ticket matching these numbers wins a prize: {ticket}")

my_ticket = []

active = True
count = 0

while active:
    count = count + 1
    shuffle(seriel_number)
    my_ticket = seriel_number[0:4]
    print(f"try{count}: number {my_ticket}")
    if my_ticket == ticket:

        print(f"you have won the prize in {count} trys")
        break
