def greet_users(names):
    """ print a simple greeting to each users in a list """
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['leo','tony','jackie']
greet_users(usernames)        