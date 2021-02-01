from random import choice

seriel_number = [1,2,3,4,5,6,7,8,9,'f','h','a','s','r']
ticket = []

for i in range(4):
    pick_number = choice(seriel_number)
    ticket.append(pick_number)

print(f"any ticket matching these numbers wins a prize: {ticket}")
