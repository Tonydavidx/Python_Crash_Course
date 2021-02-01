current_users = ['leo','Naruto','jackie','itachi','tony']
new_users =['oro','donne','leo','naruto','Tony']

for n_user in new_users:
    if n_user in current_users:
        print("The username "+ n_user + ' is not available')
    elif n_user.lower() in current_users:
        print("The username "+ n_user + ' is not available')
    elif n_user.upper() in current_users:
        print("The username "+ n_user + ' is not available')
    elif n_user.title() in current_users:
        print("The username "+ n_user + ' is not available')    
    else:
        print("username "+ n_user + " is available for use")     