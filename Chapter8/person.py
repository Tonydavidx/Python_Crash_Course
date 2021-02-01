def build_person(first_name,last_name):
    """ return a dictionary of informations about a person """
    person = {'first':first_name, 'last': last_name}
    return person

musician = build_person('antony','david')    
print(musician)
