def buil_profile(first,last,**user_info):
    """ building a dictionary everything we know about a user """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = buil_profile('albert', 'einstein', 
                            location='princton',
                                field='physics')

print(user_profile)