person_1 = {
    'first_name':'tony',
    'last_name':'david',
    'age': 19,
    'city':'avadi',
}
person_2 = {
    'first_name':'itachi',
    'last_name':'uchia',
    'age': 19,
    'city':'konaha',
}
person_3 = {
    'first_name':'Dan',
    'last_name':'Brown',
    'age': 45,
    'city':'New york',
}
peoples = [person_1,person_2,person_3]
blocker_users = ['itachi uchia']

for bu in blocker_users:
    for people in peoples:
        name = people['first_name']+ " " + people['last_name']
        if name in bu:
            print("you are not allowed here itachi Uchia")
        else:
            print(name+" thank you for visiting konaha")
 