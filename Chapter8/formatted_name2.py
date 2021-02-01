def get_formatted_name(first_name, last_name, middle_name = ''):
    """ return full name """
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title() #i still understand how return works

name = get_formatted_name('antony','david')
print(name)

name = get_formatted_name('rahul','sharad','dravid')
print(name)

 