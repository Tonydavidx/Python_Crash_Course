favorite_places = {
    'tony' : ['japan','disney land'],
    'leon' : ['milan','florence'],
    'itachi':['Konaha'],
}
for n,places in favorite_places.items():
    if len(places) >= 2:
        print(n+"'s Favorite places is :")
    else:
         print(n+"'s Favorite Place is :")   
    for place in places:
        print(place)