def formatted_name(first_name,last_name):
    """return a full name neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = formatted_name('anthony','david')
print(musician)

""" When you call a function that returns a value, you need to provide a variable that the return value can be assigned to. In this case, the returned value is assigned to the variable musician """
