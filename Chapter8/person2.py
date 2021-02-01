def build_person(first_name,last_name,age=None):
    """ return a dictionary of informations about a person """
    person = {'first':first_name, 'last': last_name}
    # this code tell if age is true add age to the dictonary
    if age: 
        person['age'] = age
    return person

musician = build_person('antony','david')    
print(musician)
