users = {
    'aeinstein':{
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princton',
    },
    'ntesla' : {
        'first' :'nikola',
        'last' : 'tesla',
        'location' : 'new york',
    },
}

for username, userinfo in users.items():
    print("\nUsername: " + username)
    fullname = userinfo['first'] +" " + userinfo['last']
    location = userinfo['location']

    print("\tFull Name: "+fullname.title())
    print("\tLocation: "+location.title())    