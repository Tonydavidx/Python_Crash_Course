person_1 = {
    'first_name':'tony',
    'last_name':'david',
    'age': 19,
    'city':'avadi',
}
person_2 = {
    'first_name':'naruto',
    'last_name':'uzumaki',
    'age': 15,
    'city':'konaga',
}
person_3 = {
    'first_name':'harry',
    'last_name':'potter',
    'age': 25,
    'city':'london',
}
peoples = [person_1,person_2,person_3]

for people in peoples:
    fullname = people['first_name'].title()+" " + people['last_name'].title()
    age = people['age']
    city = people['city'].title()
    print("users Full name: " +fullname)
    print("Age: "+str(age))
    print("City: "+city)    