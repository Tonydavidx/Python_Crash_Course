# start with unconfirmed users list and empty list to hold confirmed users 
unconfirmed_users = ['alice','leon','itachi']
confirmed_users = []

# verify each user until there are no unconfirmed user
# move each verified user into the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"veifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# display all confirmed users
print("\nthe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())     
