import json

def get_stored_username():
    """ check if the username is available in a file """
    filename = 'username.json'
    try:
        with open(filename) as file:
            user = json.load(file)
    except:
        return None

    else:
        return user        

def get_new_username():
    """ get a new username if not already exists  """
    user = input("what is your name? ")
    filename = 'username.json'
    with open (filename, 'w') as file:
        json.dump(user, file)

    return user

def greet_user():
    """ Greet user by name """
    user = get_stored_username()
    verify = input(f"are you {user} (yes / no)")
    if verify.lower() == 'yes':
        print(f"welcome back, {user}")
    else:
        user = get_new_username()
        print(f"we will remember you when you get back {user}")   

greet_user()
