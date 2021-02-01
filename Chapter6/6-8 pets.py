pet_1 = {
    'animal' : 'dog',
    'owner' : 'tony',
}
pet_2 = {
    'animal' : 'cat',
    'owner' : 'jes',
}
pet_3 = {
    'animal' : 'parrot',
    'owner' : 'stark',
}

pets = [pet_1,pet_2,pet_3]

for pet in pets:
    kind = pet['animal'].title()
    own = pet['owner'].title()
    print(own+"'s pet is a "+kind)