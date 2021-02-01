def get_formatted_name(first_name,last_name):
    """return a full name neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#this is an infinite loop!
while True:
    print("\ntell me your name: ")
    print("enter Q to quit at any time")
 
    f_name = input("first name: ")
    if f_name == 'q':
        break

    l_name = input("last name :")
    if l_name == 'q':
        break   
        
    formatted_name = get_formatted_name(f_name,l_name)
    print(f"\nHello, {formatted_name}!")    